import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class wave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}wave"):
                content = message.content[len(f"{data['prefix']}wave"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                await message.reply(f"""
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
{content}
 {content}
  {content}
   {content}
    {content}
     {content}
      {content}
       {content}
       {content}
      {content}
     {content}
    {content}
   {content}
  {content}
 {content}
{content}
""")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}wave` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def wave(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        await ctx.send(f"""
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
{args}
 {args}
  {args}
   {args}
    {args}
     {args}
      {args}
       {args}
       {args}
      {args}
     {args}
    {args}
   {args}
  {args}
 {args}
{args}
""")

async def setup(bot):
    await bot.add_cog(wave(bot))
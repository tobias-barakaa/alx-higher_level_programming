#!/usr/bin/node

const args = Number(process.argv[2]);
if (args)
{
  console.log(`My number: ${args}`);
}
} else
{
  console.log('Not a number');
}

#
# PySNMP MIB module NMS-SYS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-SYS
# Produced by pysmi-0.3.4 at Wed May  1 14:22:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Gauge32, Unsigned32, IpAddress, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, ObjectIdentity, Counter32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter32", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmslsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1))
nmsromId = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsromId.setStatus('mandatory')
if mibBuilder.loadTexts: nmsromId.setDescription('This variable contains a printable octet string which contains the System Bootstrap description and version identification.')
nmswhyReload = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmswhyReload.setStatus('mandatory')
if mibBuilder.loadTexts: nmswhyReload.setDescription('This variable contains a printable octet string which contains the reason why the system was last restarted.')
nmshostName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmshostName.setStatus('mandatory')
if mibBuilder.loadTexts: nmshostName.setDescription('This variable represents the name of the host in printable ascii characters.')
nmsdomainName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsdomainName.setStatus('mandatory')
if mibBuilder.loadTexts: nmsdomainName.setDescription('This variable is the domain portion of the domain name of the host.')
nmsauthAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsauthAddr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsauthAddr.setDescription('This variable contains the last SNMP authorization failure IP address.')
nmsbootHost = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbootHost.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbootHost.setDescription('Contains the IP address of the host that supplied the currently running software.')
nmsping = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsping.setStatus('obsolete')
if mibBuilder.loadTexts: nmsping.setDescription('The ping mib object is obsolete as of IOS 10.2 It has been superseded by the NMS Ping MIB')
nmsfreeMem = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsfreeMem.setStatus('obsolete')
if mibBuilder.loadTexts: nmsfreeMem.setDescription('The freeMem mib object is obsolete as of IOS 11.1 It has been replaced with the NMS memory pool mib')
nmsbufferElFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferElFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferElFree.setDescription('Contains the number of free buffer elements.')
nmsbufferElMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferElMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferElMax.setDescription('Contains the maximum number of buffer elements.')
nmsbufferElHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferElHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferElHit.setDescription('Contains the number of buffer element hits.')
nmsbufferElMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferElMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferElMiss.setDescription('Contains the number of buffer element misses.')
nmsbufferElCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferElCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferElCreate.setDescription('Contains the number of buffer element creates.')
nmsbufferSmSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmSize.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmSize.setDescription('Contains the size of small buffers.')
nmsbufferSmTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmTotal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmTotal.setDescription('Contains the total number of small buffers.')
nmsbufferSmFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmFree.setDescription('Contains the number of free small buffers.')
nmsbufferSmMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmMax.setDescription('Contains the maximum number of small buffers.')
nmsbufferSmHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmHit.setDescription('Contains the number of small buffer hits.')
nmsbufferSmMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmMiss.setDescription('Contains the number of small buffer misses.')
nmsbufferSmTrim = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmTrim.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmTrim.setDescription('Contains the number of small buffer trims.')
nmsbufferSmCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferSmCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferSmCreate.setDescription('Contains the number of small buffer creates.')
nmsbufferMdSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdSize.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdSize.setDescription('Contains the size of medium buffers.')
nmsbufferMdTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdTotal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdTotal.setDescription('Contains the total number of medium buffers.')
nmsbufferMdFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdFree.setDescription('Contains the number of free medium buffers.')
nmsbufferMdMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdMax.setDescription('Contains the maximum number of medium buffers.')
nmsbufferMdHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdHit.setDescription('Contains the number of medium buffer hits.')
nmsbufferMdMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdMiss.setDescription('Contains the number of medium buffer misses.')
nmsbufferMdTrim = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdTrim.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdTrim.setDescription('Contains the number of medium buffer trims.')
nmsbufferMdCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferMdCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferMdCreate.setDescription('Contains the number of medium buffer creates.')
nmsbufferBgSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgSize.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgSize.setDescription('Contains the size of big buffers.')
nmsbufferBgTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgTotal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgTotal.setDescription('Contains the total number of big buffers.')
nmsbufferBgFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgFree.setDescription('Contains the number of free big buffers.')
nmsbufferBgMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgMax.setDescription('Contains the maximum number of big buffers.')
nmsbufferBgHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgHit.setDescription('Contains the number of big buffer hits.')
nmsbufferBgMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgMiss.setDescription('Contains the number of big buffer misses.')
nmsbufferBgTrim = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgTrim.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgTrim.setDescription('Contains the number of big buffer trims.')
nmsbufferBgCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferBgCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferBgCreate.setDescription('Contains the number of big buffer creates.')
nmsbufferLgSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgSize.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgSize.setDescription('Contains the size of large buffers.')
nmsbufferLgTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgTotal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgTotal.setDescription('Contains the total number of large buffers.')
nmsbufferLgFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgFree.setDescription('Contains the number of free large buffers.')
nmsbufferLgMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgMax.setDescription('Contains the maximum number of large buffers.')
nmsbufferLgHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgHit.setDescription('Contains the number of large buffer hits.')
nmsbufferLgMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgMiss.setDescription('Contains the number of large buffer misses.')
nmsbufferLgTrim = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgTrim.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgTrim.setDescription('Contains the number of large buffer trims.')
nmsbufferLgCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferLgCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferLgCreate.setDescription('Contains the number of large buffer creates.')
nmsbufferFail = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferFail.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferFail.setDescription('Count of the number of buffer allocation failures.')
nmsbufferNoMem = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferNoMem.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferNoMem.setDescription('Count of the number of buffer create failures due to no free memory.')
nmsnetConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 48), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsnetConfigAddr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsnetConfigAddr.setDescription('Holds the address of the host that supplied the network-confg file.')
nmsnetConfigName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsnetConfigName.setStatus('mandatory')
if mibBuilder.loadTexts: nmsnetConfigName.setDescription('Holds the name of the network configuration file.')
nmsnetConfigSet = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 50), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsnetConfigSet.setStatus('mandatory')
if mibBuilder.loadTexts: nmsnetConfigSet.setDescription('Cause the loading of a new network-confg file using TFTP.')
nmshostConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 51), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmshostConfigAddr.setStatus('obsolete')
if mibBuilder.loadTexts: nmshostConfigAddr.setDescription('Contains the address of the host that provided the host-config file.')
nmshostConfigName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 52), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmshostConfigName.setStatus('obsolete')
if mibBuilder.loadTexts: nmshostConfigName.setDescription('Contains the name of the last configured host-confg file.')
nmshostConfigSet = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 53), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmshostConfigSet.setStatus('obsolete')
if mibBuilder.loadTexts: nmshostConfigSet.setDescription('Cause the loading of a new host-confg file using TFTP.')
nmswriteMem = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 54), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmswriteMem.setStatus('mandatory')
if mibBuilder.loadTexts: nmswriteMem.setDescription('Write configuration into non-volatile memory / erase config memory if 0.')
nmswriteNet = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 55), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmswriteNet.setStatus('mandatory')
if mibBuilder.loadTexts: nmswriteNet.setDescription('Write configuration to host using TFTP.')
nmsbusyPer = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbusyPer.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbusyPer.setDescription('CPU busy percentage in the last 5 second period. Not the last 5 realtime seconds but the last 5 second period in the scheduler.')
nmsavgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsavgBusy1.setStatus('mandatory')
if mibBuilder.loadTexts: nmsavgBusy1.setDescription('1 minute exponentially-decayed moving average of the CPU busy percentage.')
nmsavgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsavgBusy5.setStatus('mandatory')
if mibBuilder.loadTexts: nmsavgBusy5.setDescription('5 minute exponentially-decayed moving average of the CPU busy percentage.')
nmsidleCount = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsidleCount.setStatus('mandatory')
if mibBuilder.loadTexts: nmsidleCount.setDescription('NMS internal variable. not to be used')
nmsidleWired = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsidleWired.setStatus('mandatory')
if mibBuilder.loadTexts: nmsidleWired.setDescription('NMS internal variable. not to be used')
nmsContactInfo = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 61), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsContactInfo.setStatus('mandatory')
if mibBuilder.loadTexts: nmsContactInfo.setDescription("NMS's name and address")
nmsbufferHgSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 62), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgSize.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgSize.setDescription('Contains the size of huge buffers.')
nmsbufferHgTotal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 63), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgTotal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgTotal.setDescription('Contains the total number of huge buffers.')
nmsbufferHgFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 64), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgFree.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgFree.setDescription('Contains the number of free huge buffers.')
nmsbufferHgMax = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgMax.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgMax.setDescription('Contains the maximum number of huge buffers.')
nmsbufferHgHit = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 66), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgHit.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgHit.setDescription('Contains the number of huge buffer hits.')
nmsbufferHgMiss = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 67), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgMiss.setDescription('Contains the number of huge buffer misses.')
nmsbufferHgTrim = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 68), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgTrim.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgTrim.setDescription('Contains the number of huge buffer trims.')
nmsbufferHgCreate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 69), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsbufferHgCreate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsbufferHgCreate.setDescription('Contains the number of huge buffer creates.')
nmsnetConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 70), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsnetConfigProto.setStatus('mandatory')
if mibBuilder.loadTexts: nmsnetConfigProto.setDescription('Holds the protocol that supplied the network-confg file.')
nmshostConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 71), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmshostConfigProto.setStatus('mandatory')
if mibBuilder.loadTexts: nmshostConfigProto.setDescription('Holds the protocol that supplied the host- confg file.')
nmssysConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 72), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmssysConfigAddr.setStatus('mandatory')
if mibBuilder.loadTexts: nmssysConfigAddr.setDescription('Holds the address of the host that supplied the system boot image.')
nmssysConfigName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 73), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmssysConfigName.setStatus('mandatory')
if mibBuilder.loadTexts: nmssysConfigName.setDescription('Holds the name of the system boot image.')
nmssysConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 74), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmssysConfigProto.setStatus('mandatory')
if mibBuilder.loadTexts: nmssysConfigProto.setDescription('Holds the protocol that supplied the system boot image.')
nmssysClearARP = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 75), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmssysClearARP.setStatus('mandatory')
if mibBuilder.loadTexts: nmssysClearARP.setDescription('Perform a clearing of the entire ARP cache and invalidation of route caches.')
nmssysClearInt = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 76), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmssysClearInt.setStatus('mandatory')
if mibBuilder.loadTexts: nmssysClearInt.setDescription('Clear interface given IfIndex as value.')
nmsenvPresent = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 77), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvPresent.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvPresent.setDescription('Is there an environmental monitor card in this box?, 0 - No, 1-AGS card present, wrong firmware, 2-AGS CARD present, firmware ok, 3-7000 support')
nmsenvTestPt1Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 78), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt1Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt1Descr.setDescription('Description of the test point 1. Typically ambient air or the temperature of air entering the router')
nmsenvTestPt1Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 79), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt1Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt1Measure.setDescription('Current value of test point 1. Typically a temperature in centigrade.')
nmsenvTestPt2Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 80), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt2Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt2Descr.setDescription('Description of the test point 2. Typically airflow or the temperature of air leaving the router')
nmsenvTestPt2Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 81), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt2Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt2Measure.setDescription('Current value of test point 2. Typically a temperature in centigrade.')
nmsenvTestPt3Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 82), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt3Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt3Descr.setDescription('Description of the test point 3. Typically +5 volt')
nmsenvTestPt3Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 83), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt3Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt3Measure.setDescription('Current value of test point 3. Typically the value in millivolts of the +5v supply')
nmsenvTestPt4Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 84), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt4Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt4Descr.setDescription('Description of the test point 4. Typically +12 volt')
nmsenvTestPt4Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 85), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt4Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt4Measure.setDescription('Current value of test point 4. Typically the value in millivolts of the +12v supply')
nmsenvTestPt5Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 86), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt5Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt5Descr.setDescription('Description of the test point 5. Typically -12 volt')
nmsenvTestPt5Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 87), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt5Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt5Measure.setDescription('Current value of test point 5. Typically the value in millivolts of the -12v supply')
nmsenvTestPt6Descr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 88), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt6Descr.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt6Descr.setDescription('Description of the test point 6. Typically -5 volt')
nmsenvTestPt6Measure = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 89), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt6Measure.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt6Measure.setDescription('Current value of test point 6. Typically the value in millivolts of the -5v supply')
nmsenvTestPt1MarginVal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 90), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt1MarginVal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt1MarginVal.setDescription('Value at which the router will shutdown. Typically the ambient air temperature that will shut the router down. (e.g. 43)')
nmsenvTestPt2MarginVal = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 91), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt2MarginVal.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt2MarginVal.setDescription('Value at which the router will shutdown. Typically the airflow air temperature that will shut the router down. (e.g. 58)')
nmsenvTestPt3MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 92), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt3MarginPercent.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt3MarginPercent.setDescription('+/- Percentage that will shut the router down, (e.g. 10%) typically +5 volt')
nmsenvTestPt4MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 93), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt4MarginPercent.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt4MarginPercent.setDescription('+/- Percentage that will shut the router down, (e.g. 15%) typically +12 volt')
nmsenvTestPt5MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 94), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt5MarginPercent.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt5MarginPercent.setDescription('+/- Percentage that will shut the router down, (e.g. 15%) typically -12 volt')
nmsenvTestPt6MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 95), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt6MarginPercent.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt6MarginPercent.setDescription('+/- Percentage that will shut the router down, (e.g. 10%) typically -5 volt')
nmsenvTestPt1last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 96), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt1last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt1last.setDescription('Value of TestPt1 when last shutdown occurred.')
nmsenvTestPt2last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 97), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt2last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt2last.setDescription('Value of TestPt2 when last shutdown occurred.')
nmsenvTestPt3last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 98), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt3last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt3last.setDescription('Value of TestPt3 when last shutdown occurred.')
nmsenvTestPt4last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 99), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt4last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt4last.setDescription('Value of TestPt4 when last shutdown occurred.')
nmsenvTestPt5last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt5last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt5last.setDescription('Value of TestPt5 when last shutdown occurred.')
nmsenvTestPt6last = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 101), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt6last.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt6last.setDescription('Value of TestPt6 when last shutdown occurred.')
nmsenvTestPt1warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 102), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt1warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt1warn.setDescription('Is this test point at a warning level?')
nmsenvTestPt2warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt2warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt2warn.setDescription('Is this test point at a warning level?')
nmsenvTestPt3warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 104), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt3warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt3warn.setDescription('Is this test point at a warning level?')
nmsenvTestPt4warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 105), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt4warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt4warn.setDescription('Is this test point at a warning level?')
nmsenvTestPt5warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 106), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt5warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt5warn.setDescription('Is this test point at a warning level?')
nmsenvTestPt6warn = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 107), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTestPt6warn.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTestPt6warn.setDescription('Is this test point at a warning level?')
nmsenvFirmVersion = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 108), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvFirmVersion.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvFirmVersion.setDescription('Description of Environmental Card firmware')
nmsenvTechnicianID = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 109), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvTechnicianID.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvTechnicianID.setDescription('Technician ID')
nmsenvType = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 110), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvType.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvType.setDescription('The type of environmental card')
nmsenvBurnDate = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 111), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvBurnDate.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvBurnDate.setDescription('The calibration / burn in date')
nmsenvSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 112), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsenvSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: nmsenvSerialNumber.setDescription('Serial Number of environmental monitor card')
mibBuilder.exportSymbols("NMS-SYS", nmsbufferSmHit=nmsbufferSmHit, nmsbufferElCreate=nmsbufferElCreate, nmsbufferLgFree=nmsbufferLgFree, nmsenvTestPt3Measure=nmsenvTestPt3Measure, nmsbufferHgSize=nmsbufferHgSize, nmsenvTestPt2MarginVal=nmsenvTestPt2MarginVal, nmssysConfigProto=nmssysConfigProto, nmsbufferHgTotal=nmsbufferHgTotal, nmsenvTechnicianID=nmsenvTechnicianID, nmsbufferSmMax=nmsbufferSmMax, nmsenvFirmVersion=nmsenvFirmVersion, nmsenvType=nmsenvType, nmsbufferSmFree=nmsbufferSmFree, nmsbufferMdCreate=nmsbufferMdCreate, nmsenvTestPt1Measure=nmsenvTestPt1Measure, nmsbootHost=nmsbootHost, nmsnetConfigAddr=nmsnetConfigAddr, nmsbufferSmMiss=nmsbufferSmMiss, nmsbufferLgTotal=nmsbufferLgTotal, nmsbufferBgSize=nmsbufferBgSize, nmsenvTestPt1MarginVal=nmsenvTestPt1MarginVal, nmssysConfigAddr=nmssysConfigAddr, nmssysConfigName=nmssysConfigName, nmsenvTestPt5warn=nmsenvTestPt5warn, nmsbufferLgTrim=nmsbufferLgTrim, nmsenvTestPt5Descr=nmsenvTestPt5Descr, nmsenvTestPt6Measure=nmsenvTestPt6Measure, nmshostConfigProto=nmshostConfigProto, nmsbufferFail=nmsbufferFail, nmsdomainName=nmsdomainName, nmsenvTestPt1last=nmsenvTestPt1last, nmsbufferMdTotal=nmsbufferMdTotal, nmsbufferElFree=nmsbufferElFree, nmsbufferHgFree=nmsbufferHgFree, nmswriteNet=nmswriteNet, nmsbufferBgHit=nmsbufferBgHit, nmsauthAddr=nmsauthAddr, nmsenvPresent=nmsenvPresent, nmsenvTestPt4warn=nmsenvTestPt4warn, nmsbufferBgMax=nmsbufferBgMax, nmsidleCount=nmsidleCount, nmsbufferHgMiss=nmsbufferHgMiss, nmsbufferElHit=nmsbufferElHit, nmsbufferHgTrim=nmsbufferHgTrim, nmsenvTestPt5last=nmsenvTestPt5last, nmswriteMem=nmswriteMem, nmswhyReload=nmswhyReload, nmsenvTestPt6warn=nmsenvTestPt6warn, nmsbufferElMax=nmsbufferElMax, nmsavgBusy5=nmsavgBusy5, nmshostConfigName=nmshostConfigName, nmsbufferBgFree=nmsbufferBgFree, nmsnetConfigProto=nmsnetConfigProto, nmsbufferMdMax=nmsbufferMdMax, nmsnetConfigSet=nmsnetConfigSet, nmsbufferLgSize=nmsbufferLgSize, nmsenvSerialNumber=nmsenvSerialNumber, nmsbufferNoMem=nmsbufferNoMem, nmsenvTestPt6MarginPercent=nmsenvTestPt6MarginPercent, nmsbusyPer=nmsbusyPer, nmshostName=nmshostName, nmshostConfigAddr=nmshostConfigAddr, nmsenvTestPt4Descr=nmsenvTestPt4Descr, nmsbufferLgMiss=nmsbufferLgMiss, nmsbufferBgTotal=nmsbufferBgTotal, nmsbufferHgHit=nmsbufferHgHit, nmsping=nmsping, nmsbufferMdMiss=nmsbufferMdMiss, nmsidleWired=nmsidleWired, nmsbufferBgTrim=nmsbufferBgTrim, nmsbufferMdTrim=nmsbufferMdTrim, nmsnetConfigName=nmsnetConfigName, nmsenvTestPt3Descr=nmsenvTestPt3Descr, nmsenvTestPt2last=nmsenvTestPt2last, nmsenvTestPt3MarginPercent=nmsenvTestPt3MarginPercent, nmsbufferHgCreate=nmsbufferHgCreate, nmslsystem=nmslsystem, nmsbufferBgMiss=nmsbufferBgMiss, nmsContactInfo=nmsContactInfo, nmsenvTestPt2Descr=nmsenvTestPt2Descr, nmsenvTestPt6last=nmsenvTestPt6last, nmsbufferBgCreate=nmsbufferBgCreate, nmsenvTestPt2Measure=nmsenvTestPt2Measure, nmsenvTestPt5Measure=nmsenvTestPt5Measure, nmsenvTestPt1warn=nmsenvTestPt1warn, nmsenvTestPt3warn=nmsenvTestPt3warn, nmsenvTestPt1Descr=nmsenvTestPt1Descr, nmsenvTestPt4last=nmsenvTestPt4last, nmsbufferLgCreate=nmsbufferLgCreate, nmsbufferMdFree=nmsbufferMdFree, nmsenvTestPt4Measure=nmsenvTestPt4Measure, nmsenvTestPt2warn=nmsenvTestPt2warn, nmssysClearARP=nmssysClearARP, nmsbufferMdHit=nmsbufferMdHit, nmsbufferLgHit=nmsbufferLgHit, nmsfreeMem=nmsfreeMem, nmsenvTestPt5MarginPercent=nmsenvTestPt5MarginPercent, nmsenvTestPt4MarginPercent=nmsenvTestPt4MarginPercent, nmsbufferSmTotal=nmsbufferSmTotal, nmsenvTestPt6Descr=nmsenvTestPt6Descr, nmsbufferSmCreate=nmsbufferSmCreate, nmsavgBusy1=nmsavgBusy1, nmsbufferLgMax=nmsbufferLgMax, nmshostConfigSet=nmshostConfigSet, nmsbufferSmSize=nmsbufferSmSize, nmsbufferMdSize=nmsbufferMdSize, nmsromId=nmsromId, nmsbufferHgMax=nmsbufferHgMax, nmsenvBurnDate=nmsenvBurnDate, nmssysClearInt=nmssysClearInt, nmsenvTestPt3last=nmsenvTestPt3last, nmsbufferSmTrim=nmsbufferSmTrim, nmsbufferElMiss=nmsbufferElMiss)

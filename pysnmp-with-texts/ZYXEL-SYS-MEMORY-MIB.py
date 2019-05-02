#
# PySNMP MIB module ZYXEL-SYS-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-SYS-MEMORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, TimeTicks, Counter64, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelSysMemory = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50))
if mibBuilder.loadTexts: zyxelSysMemory.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelSysMemory.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelSysMemory.setContactInfo('')
if mibBuilder.loadTexts: zyxelSysMemory.setDescription('The subtree for system memory')
zyxelSysMemoryPoolStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1))
zyxelSysMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1), )
if mibBuilder.loadTexts: zyxelSysMemoryPoolTable.setStatus('current')
if mibBuilder.loadTexts: zyxelSysMemoryPoolTable.setDescription('The table that show memory utilization statistics on the switch.')
zyxelSysMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1), ).setIndexNames((0, "ZYXEL-SYS-MEMORY-MIB", "zySysMemoryPoolId"))
if mibBuilder.loadTexts: zyxelSysMemoryPoolEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelSysMemoryPoolEntry.setDescription('Memory utilization statistics information for the switch.')
zySysMemoryPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: zySysMemoryPoolId.setStatus('current')
if mibBuilder.loadTexts: zySysMemoryPoolId.setDescription('ID of the memory pool.')
zySysMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolName.setStatus('current')
if mibBuilder.loadTexts: zySysMemoryPoolName.setDescription('Name of the memory pool.')
zySysMemoryPoolTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolTotalSize.setStatus('current')
if mibBuilder.loadTexts: zySysMemoryPoolTotalSize.setDescription('Total size of memory pool in bytes.')
zySysMemoryPoolUsedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolUsedSize.setStatus('current')
if mibBuilder.loadTexts: zySysMemoryPoolUsedSize.setDescription('Used size of memory pool in bytes.')
zySysMemoryPoolUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolUtilization.setStatus('current')
if mibBuilder.loadTexts: zySysMemoryPoolUtilization.setDescription('Utilization of memory pool in bytes.')
mibBuilder.exportSymbols("ZYXEL-SYS-MEMORY-MIB", zyxelSysMemory=zyxelSysMemory, PYSNMP_MODULE_ID=zyxelSysMemory, zySysMemoryPoolId=zySysMemoryPoolId, zySysMemoryPoolTotalSize=zySysMemoryPoolTotalSize, zySysMemoryPoolName=zySysMemoryPoolName, zyxelSysMemoryPoolStatus=zyxelSysMemoryPoolStatus, zyxelSysMemoryPoolEntry=zyxelSysMemoryPoolEntry, zyxelSysMemoryPoolTable=zyxelSysMemoryPoolTable, zySysMemoryPoolUtilization=zySysMemoryPoolUtilization, zySysMemoryPoolUsedSize=zySysMemoryPoolUsedSize)

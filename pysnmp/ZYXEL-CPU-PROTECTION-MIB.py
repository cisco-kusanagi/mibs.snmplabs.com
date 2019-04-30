#
# PySNMP MIB module ZYXEL-CPU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-CPU-PROTECTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, Counter32, TimeTicks, NotificationType, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, iso, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter32", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelCpuProtection = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16))
if mibBuilder.loadTexts: zyxelCpuProtection.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelCpuProtection.setOrganization('Enterprise Solution ZyXEL')
zyxelCpuProtectionSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1))
zyxelCpuProtectionTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1), )
if mibBuilder.loadTexts: zyxelCpuProtectionTable.setStatus('current')
zyxelCpuProtectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1), ).setIndexNames((0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionPort"), (0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionReasonType"))
if mibBuilder.loadTexts: zyxelCpuProtectionEntry.setStatus('current')
zyCpuProtectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyCpuProtectionPort.setStatus('current')
zyCpuProtectionReasonType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("arp", 1), ("bpdu", 2), ("igmp", 3))))
if mibBuilder.loadTexts: zyCpuProtectionReasonType.setStatus('current')
zyCpuProtectionRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyCpuProtectionRateLimit.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-CPU-PROTECTION-MIB", zyCpuProtectionRateLimit=zyCpuProtectionRateLimit, zyCpuProtectionReasonType=zyCpuProtectionReasonType, PYSNMP_MODULE_ID=zyxelCpuProtection, zyxelCpuProtectionTable=zyxelCpuProtectionTable, zyxelCpuProtection=zyxelCpuProtection, zyxelCpuProtectionEntry=zyxelCpuProtectionEntry, zyxelCpuProtectionSetup=zyxelCpuProtectionSetup, zyCpuProtectionPort=zyCpuProtectionPort)

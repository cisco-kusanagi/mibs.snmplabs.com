#
# PySNMP MIB module JUNIPER-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, Counter32, Unsigned32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32", "Unsigned32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "MibIdentifier", "Integer32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
jnxMac = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 23))
jnxMac.setRevisions(('2002-10-10 00:00',))
if mibBuilder.loadTexts: jnxMac.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxMac.setOrganization('Juniper Networks, Inc.')
class JnxVlanIndex(TextualConvention, Unsigned32):
    status = 'current'

jnxMacStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1))
jnxMacStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1), )
if mibBuilder.loadTexts: jnxMacStatsTable.setStatus('current')
jnxMacStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-MAC-MIB", "jnxVlanIndex"), (0, "JUNIPER-MAC-MIB", "jnxSourceMacAddress"))
if mibBuilder.loadTexts: jnxMacStatsEntry.setStatus('current')
jnxVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 1), JnxVlanIndex())
if mibBuilder.loadTexts: jnxVlanIndex.setStatus('current')
jnxSourceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: jnxSourceMacAddress.setStatus('current')
jnxMacHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInOctets.setStatus('current')
jnxMacHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInFrames.setStatus('current')
jnxMacHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutOctets.setStatus('current')
jnxMacHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutFrames.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-MAC-MIB", jnxMacHCOutFrames=jnxMacHCOutFrames, JnxVlanIndex=JnxVlanIndex, jnxMacStatsTable=jnxMacStatsTable, jnxMacHCOutOctets=jnxMacHCOutOctets, PYSNMP_MODULE_ID=jnxMac, jnxMacHCInFrames=jnxMacHCInFrames, jnxMacStats=jnxMacStats, jnxSourceMacAddress=jnxSourceMacAddress, jnxMacHCInOctets=jnxMacHCInOctets, jnxMacStatsEntry=jnxMacStatsEntry, jnxVlanIndex=jnxVlanIndex, jnxMac=jnxMac)

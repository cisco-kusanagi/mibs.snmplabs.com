#
# PySNMP MIB module ELTEX-MES-IP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IP
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, iso, Integer32, MibIdentifier, Unsigned32, Counter64, NotificationType, Gauge32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "iso", "Integer32", "MibIdentifier", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "Bits", "TimeTicks")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
eltMesIpSpec = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91))
eltMesIpSpec.setRevisions(('2006-06-22 00:00',))
if mibBuilder.loadTexts: eltMesIpSpec.setLastUpdated('201402120000Z')
if mibBuilder.loadTexts: eltMesIpSpec.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1))
eltMesIcmpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2))
eltIpIcmpPacketTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpIcmpPacketTable.setStatus('current')
eltIpIcmpPacketEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltIpIcmpPacketEntry.setStatus('current')
eltIpIcmpPacketUnreachableSendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpIcmpPacketUnreachableSendEnable.setStatus('current')
eltMesArpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3))
mibBuilder.exportSymbols("ELTEX-MES-IP", eltMesArpSpec=eltMesArpSpec, eltIpIcmpPacketTable=eltIpIcmpPacketTable, eltMesIcmpSpec=eltMesIcmpSpec, eltMesIpSpec=eltMesIpSpec, eltMesOspf=eltMesOspf, eltIpIcmpPacketUnreachableSendEnable=eltIpIcmpPacketUnreachableSendEnable, eltIpIcmpPacketEntry=eltIpIcmpPacketEntry, PYSNMP_MODULE_ID=eltMesIpSpec)

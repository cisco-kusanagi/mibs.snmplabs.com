#
# PySNMP MIB module ELTEX-MES-IP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IP
# Produced by pysmi-0.3.4 at Wed May  1 13:00:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, MibIdentifier, Gauge32, IpAddress, Counter32, TimeTicks, Unsigned32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "MibIdentifier", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "Integer32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
eltMesIpSpec = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91))
eltMesIpSpec.setRevisions(('2006-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesIpSpec.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: eltMesIpSpec.setLastUpdated('201402120000Z')
if mibBuilder.loadTexts: eltMesIpSpec.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesIpSpec.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesIpSpec.setDescription('The private MIB module definition for IP MIB.')
eltMesOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1))
eltMesIcmpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2))
eltIpIcmpPacketTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpIcmpPacketTable.setStatus('current')
if mibBuilder.loadTexts: eltIpIcmpPacketTable.setDescription('This table controls the ability to send ICMP packets.')
eltIpIcmpPacketEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltIpIcmpPacketEntry.setStatus('current')
if mibBuilder.loadTexts: eltIpIcmpPacketEntry.setDescription('This entry controls the ability of interface to send ICMP packets.')
eltIpIcmpPacketUnreachableSendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpIcmpPacketUnreachableSendEnable.setStatus('current')
if mibBuilder.loadTexts: eltIpIcmpPacketUnreachableSendEnable.setDescription('ICMP Destination Unreachable packets sending is enabled or not on this interface.')
eltMesArpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3))
mibBuilder.exportSymbols("ELTEX-MES-IP", eltIpIcmpPacketEntry=eltIpIcmpPacketEntry, PYSNMP_MODULE_ID=eltMesIpSpec, eltMesOspf=eltMesOspf, eltIpIcmpPacketUnreachableSendEnable=eltIpIcmpPacketUnreachableSendEnable, eltMesIcmpSpec=eltMesIcmpSpec, eltMesArpSpec=eltMesArpSpec, eltMesIpSpec=eltMesIpSpec, eltIpIcmpPacketTable=eltIpIcmpPacketTable)

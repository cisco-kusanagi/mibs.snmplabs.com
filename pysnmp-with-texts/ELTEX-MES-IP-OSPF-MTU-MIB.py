#
# PySNMP MIB module ELTEX-MES-IP-OSPF-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IP-OSPF-MTU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, Gauge32, iso, Integer32, ObjectIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "Gauge32", "iso", "Integer32", "ObjectIdentity", "Unsigned32", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
eltMesIpOspfMtu = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4))
eltMesIpOspfMtu.setRevisions(('2013-08-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesIpOspfMtu.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesIpOspfMtu.setLastUpdated('201308300000Z')
if mibBuilder.loadTexts: eltMesIpOspfMtu.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesIpOspfMtu.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesIpOspfMtu.setDescription('This private MIB module defines End of Eltex private MIBs.')
eltIpOspfMtuTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1), )
if mibBuilder.loadTexts: eltIpOspfMtuTable.setStatus('current')
if mibBuilder.loadTexts: eltIpOspfMtuTable.setDescription('')
eltIpOspfMtuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1), ).setIndexNames((0, "ELTEX-MES-IP-OSPF-MTU-MIB", "ipAddr"))
if mibBuilder.loadTexts: eltIpOspfMtuEntry.setStatus('current')
if mibBuilder.loadTexts: eltIpOspfMtuEntry.setDescription('')
ipAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('deprecated')
if mibBuilder.loadTexts: ipAddr.setDescription('')
ipOspfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 10218))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipOspfMtu.setStatus('deprecated')
if mibBuilder.loadTexts: ipOspfMtu.setDescription('')
ipOspfMtuRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipOspfMtuRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipOspfMtuRowStatus.setDescription('The status of the row. The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated. ')
mibBuilder.exportSymbols("ELTEX-MES-IP-OSPF-MTU-MIB", PYSNMP_MODULE_ID=eltMesIpOspfMtu, ipAddr=ipAddr, eltIpOspfMtuTable=eltIpOspfMtuTable, eltMesIpOspfMtu=eltMesIpOspfMtu, ipOspfMtu=ipOspfMtu, ipOspfMtuRowStatus=ipOspfMtuRowStatus, eltIpOspfMtuEntry=eltIpOspfMtuEntry)

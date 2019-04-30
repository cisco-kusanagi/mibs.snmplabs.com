#
# PySNMP MIB module ELTEX-MES-IP-OSPF-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IP-OSPF-MTU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, IpAddress, Bits, iso, TimeTicks, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "IpAddress", "Bits", "iso", "TimeTicks", "Counter32", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
eltMesIpOspfMtu = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4))
eltMesIpOspfMtu.setRevisions(('2013-08-30 00:00',))
if mibBuilder.loadTexts: eltMesIpOspfMtu.setLastUpdated('201308300000Z')
if mibBuilder.loadTexts: eltMesIpOspfMtu.setOrganization('Eltex Enterprise Co, Ltd.')
eltIpOspfMtuTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1), )
if mibBuilder.loadTexts: eltIpOspfMtuTable.setStatus('current')
eltIpOspfMtuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1), ).setIndexNames((0, "ELTEX-MES-IP-OSPF-MTU-MIB", "ipAddr"))
if mibBuilder.loadTexts: eltIpOspfMtuEntry.setStatus('current')
ipAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('deprecated')
ipOspfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 10218))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipOspfMtu.setStatus('deprecated')
ipOspfMtuRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipOspfMtuRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-IP-OSPF-MTU-MIB", eltIpOspfMtuEntry=eltIpOspfMtuEntry, ipOspfMtuRowStatus=ipOspfMtuRowStatus, PYSNMP_MODULE_ID=eltMesIpOspfMtu, ipAddr=ipAddr, eltMesIpOspfMtu=eltMesIpOspfMtu, ipOspfMtu=ipOspfMtu, eltIpOspfMtuTable=eltIpOspfMtuTable)

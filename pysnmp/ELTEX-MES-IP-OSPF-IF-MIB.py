#
# PySNMP MIB module ELTEX-MES-IP-OSPF-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IP-OSPF-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
eltMesOspf, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesOspf")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, iso, IpAddress, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, ObjectIdentity, MibIdentifier, TimeTicks, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "iso", "IpAddress", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Bits", "NotificationType")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
eltIpOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2), )
if mibBuilder.loadTexts: eltIpOspfIfTable.setStatus('current')
eltIpOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1), ).setIndexNames((0, "ELTEX-MES-IP-OSPF-IF-MIB", "eltOspfIfAddress"))
if mibBuilder.loadTexts: eltIpOspfIfEntry.setStatus('current')
eltOspfIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfAddress.setStatus('current')
eltOspfIfPassiveDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveDefault.setStatus('current')
eltOspfIfPassiveList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveList.setStatus('current')
eltOspfIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltOspfIfStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-IP-OSPF-IF-MIB", eltOspfIfAddress=eltOspfIfAddress, eltOspfIfStatus=eltOspfIfStatus, eltOspfIfPassiveDefault=eltOspfIfPassiveDefault, eltOspfIfPassiveList=eltOspfIfPassiveList, eltIpOspfIfTable=eltIpOspfIfTable, eltIpOspfIfEntry=eltIpOspfIfEntry)

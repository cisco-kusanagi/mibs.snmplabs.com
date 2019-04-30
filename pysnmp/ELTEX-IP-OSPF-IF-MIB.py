#
# PySNMP MIB module ELTEX-IP-OSPF-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-IP-OSPF-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
eltMesOspf, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesOspf")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, ObjectIdentity, Counter32, Unsigned32, MibIdentifier, Counter64, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "MibIdentifier", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "IpAddress")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
eltIpOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2), )
if mibBuilder.loadTexts: eltIpOspfIfTable.setStatus('current')
eltIpOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1), ).setIndexNames((0, "ELTEX-IP-OSPF-IF-MIB", "eltOspfIfAddress"))
if mibBuilder.loadTexts: eltIpOspfIfEntry.setStatus('current')
eltOspfIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfAddress.setStatus('current')
eltOspfIfPassiveDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveDefault.setStatus('current')
eltOspfIfPassiveList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveList.setStatus('current')
eltOspfIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltOspfIfStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-IP-OSPF-IF-MIB", eltOspfIfAddress=eltOspfIfAddress, eltOspfIfPassiveDefault=eltOspfIfPassiveDefault, eltIpOspfIfTable=eltIpOspfIfTable, eltOspfIfStatus=eltOspfIfStatus, eltIpOspfIfEntry=eltIpOspfIfEntry, eltOspfIfPassiveList=eltOspfIfPassiveList)

#
# PySNMP MIB module STN-VTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-VTI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, Integer32, Counter32, Gauge32, ObjectIdentity, iso, Bits, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Integer32", "Counter32", "Gauge32", "ObjectIdentity", "iso", "Bits", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnRouterVTI, = mibBuilder.importSymbols("STN-ROUTER-MIB", "stnRouterVTI")
stnVti = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1))
if mibBuilder.loadTexts: stnVti.setLastUpdated('0011270000Z')
if mibBuilder.loadTexts: stnVti.setOrganization('Spring Tide Networks')
stnVtiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1))
stnVtiTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1), )
if mibBuilder.loadTexts: stnVtiTable.setStatus('current')
stnVtiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1), ).setIndexNames((0, "STN-VTI-MIB", "stnVtiIfIndex"))
if mibBuilder.loadTexts: stnVtiEntry.setStatus('current')
stnVtiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiIfIndex.setStatus('current')
stnVtiViId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiViId.setStatus('current')
stnVtiName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiName.setStatus('current')
stnVtiPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiPolicy.setStatus('current')
stnVtiState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiState.setStatus('current')
stnVtiLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiLastError.setStatus('current')
stnVtiProxyTunnelSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiProxyTunnelSerialNum.setStatus('current')
stnVtiMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiMTU.setStatus('current')
stnVtiSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiSpeed.setStatus('current')
stnVtiL2MuxIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 10), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnVtiL2MuxIdx.setStatus('current')
mibBuilder.exportSymbols("STN-VTI-MIB", stnVtiObjects=stnVtiObjects, stnVtiViId=stnVtiViId, stnVti=stnVti, stnVtiPolicy=stnVtiPolicy, stnVtiSpeed=stnVtiSpeed, stnVtiL2MuxIdx=stnVtiL2MuxIdx, stnVtiProxyTunnelSerialNum=stnVtiProxyTunnelSerialNum, stnVtiEntry=stnVtiEntry, stnVtiTable=stnVtiTable, stnVtiIfIndex=stnVtiIfIndex, stnVtiName=stnVtiName, stnVtiState=stnVtiState, stnVtiLastError=stnVtiLastError, stnVtiMTU=stnVtiMTU, PYSNMP_MODULE_ID=stnVti)

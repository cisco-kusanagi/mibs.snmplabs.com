#
# PySNMP MIB module IPAD-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPAD-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:55:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ipad, = mibBuilder.importSymbols("IPADv2-MIB", "ipad")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Integer32, Unsigned32, Counter32, IpAddress, Bits, ObjectIdentity, Gauge32, Counter64, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Integer32", "Unsigned32", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "Counter64", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipadBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 321, 100, 1, 28))
if mibBuilder.loadTexts: ipadBridge.setLastUpdated('0003270001Z')
if mibBuilder.loadTexts: ipadBridge.setOrganization('Verilink Corporation')
if mibBuilder.loadTexts: ipadBridge.setContactInfo('support@verilink.com 1-800-926-0085')
if mibBuilder.loadTexts: ipadBridge.setDescription('The IPAD BRIDGE MIB.')
ipadBridgeParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1))
ipadBridgeManagementMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgeManagementMacAddress.setStatus('current')
if mibBuilder.loadTexts: ipadBridgeManagementMacAddress.setDescription('')
ipadBridgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgeEnable.setStatus('current')
if mibBuilder.loadTexts: ipadBridgeEnable.setDescription('')
ipadBridgePortTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2), )
if mibBuilder.loadTexts: ipadBridgePortTable.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortTable.setDescription('Table of Bridge parameters.')
ipadBridgePortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1), ).setIndexNames((0, "IPAD-BRIDGE-MIB", "ipadBridgePortIndex"))
if mibBuilder.loadTexts: ipadBridgePortTableEntry.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortTableEntry.setDescription('An entry in the ipad Bridge port table.')
ipadBridgePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadBridgePortIndex.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortIndex.setDescription('The index into the Bridge table.')
ipadBridgePortEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortEndpoint.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortEndpoint.setDescription('')
ipadBridgePortBPDUOption = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortBPDUOption.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortBPDUOption.setDescription('')
ipadBridgePortMulticastAddrDest = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("no", 2), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortMulticastAddrDest.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortMulticastAddrDest.setDescription('')
ipadBridgePortBroadcastAddrDest = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("no", 2), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortBroadcastAddrDest.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortBroadcastAddrDest.setDescription('')
ipadBridgePortForwardIpFramesOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("no", 2), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortForwardIpFramesOnly.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortForwardIpFramesOnly.setDescription('')
ipadBridgePortAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortAdd.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortAdd.setDescription('')
ipadBridgePortDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadBridgePortDelete.setStatus('current')
if mibBuilder.loadTexts: ipadBridgePortDelete.setDescription('')
mibBuilder.exportSymbols("IPAD-BRIDGE-MIB", ipadBridgePortBPDUOption=ipadBridgePortBPDUOption, ipadBridgePortDelete=ipadBridgePortDelete, ipadBridgePortMulticastAddrDest=ipadBridgePortMulticastAddrDest, ipadBridgePortTable=ipadBridgePortTable, ipadBridgePortForwardIpFramesOnly=ipadBridgePortForwardIpFramesOnly, PYSNMP_MODULE_ID=ipadBridge, ipadBridge=ipadBridge, ipadBridgePortIndex=ipadBridgePortIndex, ipadBridgeManagementMacAddress=ipadBridgeManagementMacAddress, ipadBridgePortBroadcastAddrDest=ipadBridgePortBroadcastAddrDest, ipadBridgePortAdd=ipadBridgePortAdd, ipadBridgeEnable=ipadBridgeEnable, ipadBridgeParms=ipadBridgeParms, ipadBridgePortEndpoint=ipadBridgePortEndpoint, ipadBridgePortTableEntry=ipadBridgePortTableEntry)

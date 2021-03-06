#
# PySNMP MIB module XYLAN-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, Counter32, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, MibIdentifier, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter32", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanVportArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanVportArch")
virtualPort = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 3, 1))
logicalPort = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 3, 2))
physicalPort = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 3, 3))
mirrorPort = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 3, 4))
echannelPort = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 3, 5))
class XylanPortFuncCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("router", 3), ("bridge", 4), ("trunk", 5), ("atmtrunk", 6), ("atmLANE", 7), ("cip", 8), ("atmMUX", 9), ("vlmp80210", 10), ("frtrunking", 12), ("vlmpDBr", 13), ("vlmp8021q", 14), ("lsm", 15), ("phyeth", 203), ("phyx100eth", 204), ("phytr4m", 205), ("phytr16m", 206), ("phyfddi", 207), ("phycddi", 208), ("phyatm25", 209), ("phyatm50", 210), ("phyds1", 211), ("phyds3", 212), ("phyoc3", 213), ("phyoc12", 214), ("phyoc48", 215))

class XylanVportAdminStatCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("disable", 1), ("enable", 2), ("delete", 3), ("create", 4), ("modify", 5))

class XylanPortOperStatCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("portDown", 2), ("portUp", 3))

class XylanVportEncapsulationCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("switch", 1), ("mediaDefault", 2), ("ethIIllc", 3), ("tunnelOption1", 4), ("tunnelOption2", 5), ("llc", 6), ("snapllc", 7), ("ethII", 8), ("snap", 9))

class XylanVportTranslationCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ethertype", 1), ("llc", 2), ("snap", 3), ("prop", 4), ("tunnel1", 5), ("tunnel2", 6))

class XylanPhyPortTypeCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("eth", 3), ("x100eth", 4), ("tr4m", 5), ("tr16m", 6), ("fddi", 7), ("cddi", 8), ("atm25", 9), ("atm50", 10), ("ds1", 11), ("ds3", 12), ("oc3", 13), ("oc12", 14), ("oc48", 15), ("wsm", 16), ("e1", 18), ("e3", 19), ("serial", 21))

class XylanPhyPortAdminStatCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disable", 1), ("enable", 2))

class XylanMirrorEnableCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disable", 1), ("enable", 2))

vportTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1), )
if mibBuilder.loadTexts: vportTable.setStatus('mandatory')
vportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1), ).setIndexNames((0, "XYLAN-PORT-MIB", "vportSlot"), (0, "XYLAN-PORT-MIB", "vportIF"), (0, "XYLAN-PORT-MIB", "vportFuncType"), (0, "XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: vportEntry.setStatus('mandatory')
vportNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportNumber.setStatus('mandatory')
vportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSlot.setStatus('mandatory')
vportIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportIF.setStatus('mandatory')
vportFuncType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 4), XylanPortFuncCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportFuncType.setStatus('mandatory')
vportFuncTypeInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportFuncTypeInstance.setStatus('mandatory')
vportVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportVlanNumber.setStatus('mandatory')
vportMACaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportMACaddress.setStatus('mandatory')
vportBridgeProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("transparent", 3), ("sourcerouting", 4), ("srtransparent", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportBridgeProtocol.setStatus('mandatory')
vportEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 9), XylanVportEncapsulationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportEncapsulation.setStatus('mandatory')
vportBrdgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("autoSwitch", 3), ("forceBridge", 4), ("forceSwitch", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportBrdgMode.setStatus('mandatory')
vportSwitchTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchTimer.setStatus('mandatory')
vportDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportDescription.setStatus('mandatory')
vportAdmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 13), XylanVportAdminStatCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportAdmStatus.setStatus('mandatory')
vportOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 14), XylanPortOperStatCodes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOperStatus.setStatus('mandatory')
vportFrameIns = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportFrameIns.setStatus('mandatory')
vportInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportInOctets.setStatus('mandatory')
vportInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportInUcastPkts.setStatus('mandatory')
vportInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportInNUcastPkts.setStatus('mandatory')
vportInBufDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportInBufDiscs.setStatus('mandatory')
vportInErrDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportInErrDiscs.setStatus('mandatory')
vportFrameOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportFrameOuts.setStatus('mandatory')
vportOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOutOctets.setStatus('mandatory')
vportOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOutUcastPkts.setStatus('mandatory')
vportOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOutNUcastPkts.setStatus('mandatory')
vportOutBufDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOutBufDiscs.setStatus('mandatory')
vportOutErrDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportOutErrDiscs.setStatus('mandatory')
vportFloodLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportFloodLimit.setStatus('mandatory')
vportVLANMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportVLANMembership.setStatus('mandatory')
vportManualMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dynamic", 1), ("manual-override-forwarding", 2), ("manual-override-blocking", 3), ("mode-not-applicable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportManualMode.setStatus('mandatory')
vportMVLANMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportMVLANMembership.setStatus('mandatory')
vportFloodLimitDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportFloodLimitDiscs.setStatus('mandatory')
vportIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vportIfIndex.setStatus('mandatory')
phyPortTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1), )
if mibBuilder.loadTexts: phyPortTable.setStatus('mandatory')
phyPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1), ).setIndexNames((0, "XYLAN-PORT-MIB", "phyPortSlot"), (0, "XYLAN-PORT-MIB", "phyPortIF"))
if mibBuilder.loadTexts: phyPortEntry.setStatus('mandatory')
phyPortSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortSlot.setStatus('mandatory')
phyPortIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortIF.setStatus('mandatory')
phyPortMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 3), XylanPhyPortTypeCodes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortMediaType.setStatus('mandatory')
phyPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phyPortDescription.setStatus('mandatory')
phyPortAdmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 5), XylanPhyPortAdminStatCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phyPortAdmStatus.setStatus('mandatory')
phyPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 6), XylanPortOperStatCodes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOperStatus.setStatus('mandatory')
phyPortFrameIns = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortFrameIns.setStatus('mandatory')
phyPortInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortInOctets.setStatus('mandatory')
phyPortInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortInUcastPkts.setStatus('mandatory')
phyPortInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortInNUcastPkts.setStatus('mandatory')
phyPortInBufDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortInBufDiscs.setStatus('mandatory')
phyPortInErrDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortInErrDiscs.setStatus('mandatory')
phyPortFrameOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortFrameOuts.setStatus('mandatory')
phyPortOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOutOctets.setStatus('mandatory')
phyPortOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOutUcastPkts.setStatus('mandatory')
phyPortOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOutNUcastPkts.setStatus('mandatory')
phyPortOutBufDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOutBufDiscs.setStatus('mandatory')
phyPortOutErrDiscs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortOutErrDiscs.setStatus('mandatory')
phyPortToInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortToInterface.setStatus('mandatory')
phyPortFddiAdmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("station", 2), ("concentrator", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phyPortFddiAdmMode.setStatus('mandatory')
phyPortFddiOpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("station", 2), ("concentrator", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: phyPortFddiOpMode.setStatus('mandatory')
phyPortFddiMacFlushMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phyPortFddiMacFlushMode.setStatus('mandatory')
mesmConfTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2), )
if mibBuilder.loadTexts: mesmConfTable.setStatus('mandatory')
mesmConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1), ).setIndexNames((0, "XYLAN-PORT-MIB", "mesmPortSlot"), (0, "XYLAN-PORT-MIB", "mesmPortIF"))
if mibBuilder.loadTexts: mesmConfEntry.setStatus('mandatory')
mesmPortSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mesmPortSlot.setStatus('mandatory')
mesmPortIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mesmPortIF.setStatus('mandatory')
mesmPortAutoNegotiate = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("non-appl", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mesmPortAutoNegotiate.setStatus('mandatory')
mesmPortAutoSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("speed-100", 1), ("speed-10", 2), ("speed-auto", 3), ("unknown", 4), ("speed-1000", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mesmPortAutoSpeed.setStatus('mandatory')
mesmPortAutoDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("full-duplex", 1), ("half-duplex", 2), ("auto-duplex", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mesmPortAutoDuplexMode.setStatus('mandatory')
mesmPortCfgSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("speed-100", 1), ("speed-10", 2), ("speed-auto", 3), ("unknown", 4), ("speed-1000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mesmPortCfgSpeed.setStatus('mandatory')
mesmPortCfgDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("full-duplex", 1), ("half-duplex", 2), ("auto-duplex", 3), ("unknown", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mesmPortCfgDuplexMode.setStatus('mandatory')
phyPortPCause = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 3, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("flood-q-stalled", 1), ("excess-retries", 2), ("excess-runts", 3))))
if mibBuilder.loadTexts: phyPortPCause.setStatus('mandatory')
vportSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2), )
if mibBuilder.loadTexts: vportSwitchTable.setStatus('mandatory')
vportSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2), ).setIndexNames((0, "XYLAN-PORT-MIB", "vportSwitchSlot"), (0, "XYLAN-PORT-MIB", "vportSwitchIF"), (0, "XYLAN-PORT-MIB", "vportSwitchFuncType"), (0, "XYLAN-PORT-MIB", "vportSwitchFuncTypeInstance"))
if mibBuilder.loadTexts: vportSwitchEntry.setStatus('mandatory')
vportSwitchSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchSlot.setStatus('mandatory')
vportSwitchIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchIF.setStatus('mandatory')
vportSwitchFuncType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 3), XylanPortFuncCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchFuncType.setStatus('mandatory')
vportSwitchFuncTypeInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchFuncTypeInstance.setStatus('mandatory')
vportSwitchipEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 5), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipEthertype.setStatus('mandatory')
vportSwitchipSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 6), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipSnap.setStatus('mandatory')
vportSwitchipxEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 7), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipxEthertype.setStatus('mandatory')
vportSwitchipxProp = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 8), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipxProp.setStatus('mandatory')
vportSwitchipxLlc = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 9), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipxLlc.setStatus('mandatory')
vportSwitchipxSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 2, 2, 10), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchipxSnap.setStatus('mandatory')
vportSwitchDefaultTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3), )
if mibBuilder.loadTexts: vportSwitchDefaultTable.setStatus('mandatory')
vportSwitchDefaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2), ).setIndexNames((0, "XYLAN-PORT-MIB", "vportSwitchDefaultIndex"))
if mibBuilder.loadTexts: vportSwitchDefaultEntry.setStatus('mandatory')
vportSwitchDefaultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ethernet", 1), ("fddi", 2), ("tokenring", 3), ("ethLanEmulation", 4), ("tokenLanEmulation", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultIndex.setStatus('mandatory')
vportSwitchDefaultipEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 2), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipEthertype.setStatus('mandatory')
vportSwitchDefaultipSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 3), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipSnap.setStatus('mandatory')
vportSwitchDefaultipxEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 4), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipxEthertype.setStatus('mandatory')
vportSwitchDefaultipxProp = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 5), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipxProp.setStatus('mandatory')
vportSwitchDefaultipxLlc = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 6), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipxLlc.setStatus('mandatory')
vportSwitchDefaultipxSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 1, 3, 2, 7), XylanVportTranslationCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vportSwitchDefaultipxSnap.setStatus('mandatory')
mirrorTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1), )
if mibBuilder.loadTexts: mirrorTable.setStatus('mandatory')
mirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1), ).setIndexNames((0, "XYLAN-PORT-MIB", "mirrorSlot"), (0, "XYLAN-PORT-MIB", "mirrorIF"), (0, "XYLAN-PORT-MIB", "mirrorFuncType"), (0, "XYLAN-PORT-MIB", "mirrorFuncTypeInstance"))
if mibBuilder.loadTexts: mirrorEntry.setStatus('mandatory')
mirrorNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorNumber.setStatus('mandatory')
mirrorSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorSlot.setStatus('mandatory')
mirrorIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorIF.setStatus('mandatory')
mirrorFuncType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 4), XylanPortFuncCodes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorFuncType.setStatus('mandatory')
mirrorFuncTypeInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorFuncTypeInstance.setStatus('mandatory')
mirrorMirroringSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mirrorMirroringSlot.setStatus('mandatory')
mirrorMirroringIF = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mirrorMirroringIF.setStatus('mandatory')
mirrorMirroringFuncType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 8), XylanPortFuncCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mirrorMirroringFuncType.setStatus('mandatory')
mirrorMirroringFuncTypeInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mirrorMirroringFuncTypeInstance.setStatus('mandatory')
mirrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 3, 4, 1, 1, 10), XylanMirrorEnableCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mirrorStatus.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-PORT-MIB", virtualPort=virtualPort, vportSwitchipxLlc=vportSwitchipxLlc, mirrorMirroringFuncTypeInstance=mirrorMirroringFuncTypeInstance, phyPortIF=phyPortIF, vportOutBufDiscs=vportOutBufDiscs, mesmConfTable=mesmConfTable, vportMACaddress=vportMACaddress, phyPortSlot=phyPortSlot, phyPortOutNUcastPkts=phyPortOutNUcastPkts, vportOutErrDiscs=vportOutErrDiscs, vportAdmStatus=vportAdmStatus, vportInNUcastPkts=vportInNUcastPkts, phyPortInNUcastPkts=phyPortInNUcastPkts, logicalPort=logicalPort, mesmPortCfgDuplexMode=mesmPortCfgDuplexMode, phyPortFddiOpMode=phyPortFddiOpMode, vportSwitchEntry=vportSwitchEntry, phyPortFrameIns=phyPortFrameIns, vportSwitchipxSnap=vportSwitchipxSnap, phyPortOperStatus=phyPortOperStatus, vportFuncTypeInstance=vportFuncTypeInstance, mirrorNumber=mirrorNumber, vportOutUcastPkts=vportOutUcastPkts, vportSwitchTimer=vportSwitchTimer, phyPortOutUcastPkts=phyPortOutUcastPkts, phyPortTable=phyPortTable, vportSwitchSlot=vportSwitchSlot, vportSwitchDefaultipEthertype=vportSwitchDefaultipEthertype, vportTable=vportTable, vportMVLANMembership=vportMVLANMembership, phyPortInBufDiscs=phyPortInBufDiscs, mirrorFuncType=mirrorFuncType, phyPortPCause=phyPortPCause, mirrorEntry=mirrorEntry, vportSwitchDefaultEntry=vportSwitchDefaultEntry, phyPortOutErrDiscs=phyPortOutErrDiscs, phyPortInErrDiscs=phyPortInErrDiscs, vportSwitchFuncTypeInstance=vportSwitchFuncTypeInstance, echannelPort=echannelPort, mirrorIF=mirrorIF, vportInUcastPkts=vportInUcastPkts, vportInOctets=vportInOctets, phyPortAdmStatus=phyPortAdmStatus, phyPortMediaType=phyPortMediaType, mesmPortSlot=mesmPortSlot, mirrorStatus=mirrorStatus, mesmPortAutoSpeed=mesmPortAutoSpeed, mesmPortCfgSpeed=mesmPortCfgSpeed, vportFloodLimitDiscs=vportFloodLimitDiscs, vportSwitchDefaultipxSnap=vportSwitchDefaultipxSnap, vportFrameOuts=vportFrameOuts, XylanPortFuncCodes=XylanPortFuncCodes, XylanMirrorEnableCodes=XylanMirrorEnableCodes, vportSwitchDefaultipxProp=vportSwitchDefaultipxProp, XylanVportTranslationCodes=XylanVportTranslationCodes, vportSwitchipxEthertype=vportSwitchipxEthertype, vportIF=vportIF, vportSwitchipxProp=vportSwitchipxProp, mesmPortAutoDuplexMode=mesmPortAutoDuplexMode, XylanPortOperStatCodes=XylanPortOperStatCodes, vportManualMode=vportManualMode, vportBridgeProtocol=vportBridgeProtocol, mesmPortIF=mesmPortIF, vportSwitchDefaultipxLlc=vportSwitchDefaultipxLlc, mirrorTable=mirrorTable, vportSwitchipSnap=vportSwitchipSnap, vportInErrDiscs=vportInErrDiscs, mirrorPort=mirrorPort, mesmPortAutoNegotiate=mesmPortAutoNegotiate, vportEntry=vportEntry, phyPortEntry=phyPortEntry, vportSwitchTable=vportSwitchTable, phyPortToInterface=phyPortToInterface, mirrorMirroringIF=mirrorMirroringIF, vportSwitchDefaultipSnap=vportSwitchDefaultipSnap, vportVlanNumber=vportVlanNumber, mirrorMirroringSlot=mirrorMirroringSlot, vportSwitchipEthertype=vportSwitchipEthertype, phyPortInOctets=phyPortInOctets, vportSlot=vportSlot, vportNumber=vportNumber, vportOutNUcastPkts=vportOutNUcastPkts, mirrorSlot=mirrorSlot, vportBrdgMode=vportBrdgMode, phyPortDescription=phyPortDescription, phyPortOutBufDiscs=phyPortOutBufDiscs, XylanVportAdminStatCodes=XylanVportAdminStatCodes, vportOperStatus=vportOperStatus, mirrorFuncTypeInstance=mirrorFuncTypeInstance, vportInBufDiscs=vportInBufDiscs, vportFrameIns=vportFrameIns, vportFuncType=vportFuncType, phyPortInUcastPkts=phyPortInUcastPkts, phyPortFddiMacFlushMode=phyPortFddiMacFlushMode, vportSwitchDefaultTable=vportSwitchDefaultTable, vportEncapsulation=vportEncapsulation, vportSwitchFuncType=vportSwitchFuncType, vportOutOctets=vportOutOctets, vportFloodLimit=vportFloodLimit, mesmConfEntry=mesmConfEntry, vportSwitchDefaultIndex=vportSwitchDefaultIndex, mirrorMirroringFuncType=mirrorMirroringFuncType, phyPortFrameOuts=phyPortFrameOuts, vportDescription=vportDescription, phyPortFddiAdmMode=phyPortFddiAdmMode, vportVLANMembership=vportVLANMembership, XylanPhyPortTypeCodes=XylanPhyPortTypeCodes, vportSwitchDefaultipxEthertype=vportSwitchDefaultipxEthertype, phyPortOutOctets=phyPortOutOctets, XylanPhyPortAdminStatCodes=XylanPhyPortAdminStatCodes, XylanVportEncapsulationCodes=XylanVportEncapsulationCodes, vportSwitchIF=vportSwitchIF, vportIfIndex=vportIfIndex, physicalPort=physicalPort)

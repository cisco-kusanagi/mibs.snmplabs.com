#
# PySNMP MIB module CISCO-WAN-ATM-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-CONN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, iso, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter64, ModuleIdentity, Unsigned32, Bits, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "iso", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "NotificationType")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
ciscoWanAtmConnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 1))
ciscoWanAtmConnMIB.setRevisions(('2003-03-30 00:00', '2002-09-18 00:00', '2002-03-24 00:00', '2001-02-09 00:00', '2001-01-03 00:00', '2000-11-15 00:00', '2000-07-17 00:00', '2000-06-19 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmConnMIB.setLastUpdated('200303300000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnMIB.setOrganization('Cisco Systems, Inc.')
cwConnMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1))
cwAtmChanCnfg = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1))
cwAtmChanState = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2))
cwAtmChanTest = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3))
cwAtmChanInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4))
cwGlobalChanDataGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5))
class CiscoAtmServiceCategory(TextualConvention, Integer32):
    reference = 'ATM Forum Traffic Management Specification Version 4.0 Section 4.5.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("cbr1", 1), ("vbr1RT", 2), ("vbr2RT", 3), ("vbr3RT", 4), ("vbr1nRT", 5), ("vbr2nRT", 6), ("vbr3nRT", 7), ("ubr1", 8), ("ubr2", 9), ("abr", 10), ("cbr2", 11), ("cbr3", 12))

class CiscoWanLpbkTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noLpbk", 1), ("destructive", 2), ("nonDestructive", 3))

class CiscoWanLpbkDir(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("external", 1), ("internal", 2), ("forward", 3), ("reverse", 4))

class CiscoWanTestStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noStatus", 1), ("lpbkInProgress", 2), ("lpbkSuccess", 3), ("lpbkAbort", 4), ("lpbkTimeOut", 5), ("lpbkInEffect", 6))

class CiscoWanOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("operOk", 1), ("operFail", 2), ("adminDown", 3))

class CiscoWanNsapAtmAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class CiscoWanAlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("ingAisRdi", 1), ("egrAisRdi", 2), ("conditioned", 4), ("interfaceFail", 8), ("ccFail", 16), ("mismatch", 32), ("ingAbitFail", 64))

class CiscoWanXmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("sendingAIS", 2), ("sendingRDI", 3))

class CiscoWanRcvState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("receivingRDI", 2), ("receivingAIS", 3), ("ccFailure", 4))

class CiscoWanERSConfg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("enableIngress", 2), ("enableEgress", 3), ("enableBoth", 4))

class CiscoWanVSVDConfg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vsvdOff", 1), ("vsvdOn", 2), ("switchDefault", 3))

class CiscoWanAisIW(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("e2eAisCapable", 1), ("segAisCapable", 2))

class AbrRateFactors(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("oneOver32768", 1), ("oneOver16384", 2), ("oneOver8192", 3), ("oneOver4096", 4), ("oneOver2048", 5), ("oneOver1024", 6), ("oneOver512", 7), ("oneOver256", 8), ("oneOver128", 9), ("oneOver64", 10), ("oneOver32", 11), ("oneOver16", 12), ("oneOver8", 13), ("oneOver4", 14), ("oneOver2", 15), ("one", 16))

cwAtmChanCnfgTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1), )
if mibBuilder.loadTexts: cwAtmChanCnfgTable.setStatus('current')
cwAtmChanCnfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"))
if mibBuilder.loadTexts: cwAtmChanCnfgEntry.setStatus('current')
cwaChanVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: cwaChanVpi.setStatus('current')
cwaChanVci = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cwaChanVci.setStatus('current')
cwaChanServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 3), CiscoAtmServiceCategory()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanServiceCategory.setStatus('current')
cwaChanVpcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanVpcFlag.setStatus('current')
cwaChanIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanIdentifier.setStatus('current')
cwaChanUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanUploadCounter.setStatus('current')
cwaChanStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanStatsEnable.setStatus('current')
cwaChanCCEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanCCEnable.setStatus('current')
cwaChanLocalVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanLocalVpi.setStatus('current')
cwaChanLocalVci = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanLocalVci.setStatus('current')
cwaChanLocalNSAPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 11), CiscoWanNsapAtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanLocalNSAPAddr.setStatus('current')
cwaChanRemoteVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteVpi.setStatus('current')
cwaChanRemoteVci = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteVci.setStatus('current')
cwaChanRemoteNSAPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 14), CiscoWanNsapAtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteNSAPAddr.setStatus('current')
cwaChanControllerId = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanControllerId.setStatus('current')
cwaChanRoutingMastership = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRoutingMastership.setStatus('current')
cwaChanMaxCost = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(4294967295)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanMaxCost.setStatus('current')
cwaChanReroute = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanReroute.setStatus('current')
cwaChanFrameDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanFrameDiscard.setStatus('current')
cwaChanOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 20), CiscoWanOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanOperStatus.setStatus('current')
cwaChanPCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanPCR.setStatus('current')
cwaChanMCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanMCR.setStatus('current')
cwaChanSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanSCR.setStatus('current')
cwaChanCDV = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215)).clone(16777215)).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanCDV.setStatus('current')
cwaChanCTD = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanCTD.setStatus('current')
cwaChanMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 26), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000000))).setUnits('cells').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanMBS.setStatus('current')
cwaChanCDVT = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 27), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(4294967295)).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanCDVT.setStatus('current')
cwaChanPercentUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanPercentUtil.setStatus('current')
cwaChanRemotePCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 29), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemotePCR.setStatus('current')
cwaChanRemoteMCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 30), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteMCR.setStatus('current')
cwaChanRemoteSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 31), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteSCR.setStatus('current')
cwaChanRemoteCDV = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 32), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215)).clone(16777215)).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteCDV.setStatus('current')
cwaChanRemoteCTD = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 33), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteCTD.setStatus('current')
cwaChanRemoteMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 34), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000000))).setUnits('cells').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteMBS.setStatus('current')
cwaChanRemoteCDVT = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 35), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(4294967295)).setUnits('cells').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteCDVT.setStatus('deprecated')
cwaChanRemotePercentUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 36), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemotePercentUtil.setStatus('current')
cwaChanAbrICR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 37), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('cells/sec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrICR.setStatus('current')
cwaChanAbrADTF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 38), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setUnits('10 milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrADTF.setStatus('current')
cwaChanAbrRDF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 39), AbrRateFactors()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrRDF.setStatus('current')
cwaChanAbrRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 40), AbrRateFactors()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrRIF.setStatus('current')
cwaChanAbrNRM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("nrm2", 1), ("nrm4", 2), ("nrm8", 3), ("nrm16", 4), ("nrm32", 5), ("nrm64", 6), ("nrm128", 7), ("nrm256", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrNRM.setStatus('current')
cwaChanAbrTRM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("trm0point78125", 1), ("trm1point5625", 2), ("trm3point125", 3), ("trm6point25", 4), ("trm12point5", 5), ("trm25", 6), ("trm50", 7), ("trm100", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrTRM.setStatus('current')
cwaChanAbrCDF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("cdf0", 1), ("cdfOneOver64", 2), ("cdfOneOver32", 3), ("cdfOneOver16", 4), ("cdfOneOver8", 5), ("cdfOneOver4", 6), ("cdfOneOver2", 7), ("cdfOne", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrCDF.setStatus('current')
cwaChanAbrFRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 44), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16700000))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrFRTT.setStatus('current')
cwaChanAbrTBE = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 45), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrTBE.setStatus('current')
cwaChanAbrERS = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 46), CiscoWanERSConfg().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrERS.setStatus('deprecated')
cwaChanAbrVSVDEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 47), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAbrVSVDEnable.setStatus('current')
cwaChanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 48), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRowStatus.setStatus('current')
cwaChanIntAbrVSVD = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 49), CiscoWanVSVDConfg().clone('switchDefault')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanIntAbrVSVD.setStatus('current')
cwaChanExtAbrVSVD = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 50), CiscoWanVSVDConfg().clone('switchDefault')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanExtAbrVSVD.setStatus('current')
cwaChanAisIWCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 51), CiscoWanAisIW().clone('e2eAisCapable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanAisIWCapability.setStatus('deprecated')
cwaChanCLR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 52), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanCLR.setStatus('current')
cwaChanRemoteCLR = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 53), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRemoteCLR.setStatus('current')
cwaChanOamSegEpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oamSegEp", 1), ("nonOamSegEp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanOamSegEpEnable.setStatus('current')
cwaChanSlaveType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 55), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("persistentSlave", 1), ("nonPersistentSlave", 2))).clone('persistentSlave')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanSlaveType.setStatus('current')
cwaChanRoutingPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 56), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanRoutingPriority.setStatus('current')
cwaChanP2MP = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 57), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanP2MP.setStatus('current')
cwaChanPrefRouteId = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 58), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanPrefRouteId.setStatus('current')
cwaChanDirectRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 59), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaChanDirectRoute.setStatus('current')
cwAtmChanStateTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1), )
if mibBuilder.loadTexts: cwAtmChanStateTable.setStatus('current')
cwAtmChanStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"))
if mibBuilder.loadTexts: cwAtmChanStateEntry.setStatus('current')
cwaChanAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 1), CiscoWanAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanAlarmState.setStatus('current')
cwaChanEgressXmtState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 2), CiscoWanXmtState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanEgressXmtState.setStatus('current')
cwaChanEgressRcvState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 3), CiscoWanRcvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanEgressRcvState.setStatus('current')
cwaChanIngressXmtState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 4), CiscoWanXmtState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanIngressXmtState.setStatus('current')
cwaChanIngressRcvState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 5), CiscoWanRcvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanIngressRcvState.setStatus('current')
cwAtmChanTestTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1), )
if mibBuilder.loadTexts: cwAtmChanTestTable.setStatus('current')
cwAtmChanTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"), (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"))
if mibBuilder.loadTexts: cwAtmChanTestEntry.setStatus('current')
cwaChanTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 1), CiscoWanLpbkTypes().clone('noLpbk')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaChanTestType.setStatus('current')
cwaChanTestDir = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 2), CiscoWanLpbkDir()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaChanTestDir.setStatus('current')
cwaChanTestIterations = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaChanTestIterations.setStatus('current')
cwaChanTestState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 4), CiscoWanTestStatus().clone('noStatus')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanTestState.setStatus('current')
cwaChanTestRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000000))).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanTestRoundTripDelay.setStatus('current')
cwaChanNumVPCsInAlarm = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanNumVPCsInAlarm.setStatus('current')
cwaChanNumVCCsInAlarm = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwaChanNumVCCsInAlarm.setStatus('current')
cwGlobalChanDataTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1), )
if mibBuilder.loadTexts: cwGlobalChanDataTable.setStatus('current')
cwGlobalChanDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-CONN-MIB", "cwSlotIndex"))
if mibBuilder.loadTexts: cwGlobalChanDataEntry.setStatus('current')
cwSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 429496729)))
if mibBuilder.loadTexts: cwSlotIndex.setStatus('current')
cwChanGlobalTransactionId = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwChanGlobalTransactionId.setStatus('current')
ciscoWanAtmConnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 2))
ciscoWanAtmConnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1))
ciscoWanAtmConnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2))
ciscoWanAtmConnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnChanMIBGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnStateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnMIBCompliance = ciscoWanAtmConnMIBCompliance.setStatus('deprecated')
ciscoWanAtmConnMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 2)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnChan2MIBGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnStateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnMIBCompliance2 = ciscoWanAtmConnMIBCompliance2.setStatus('deprecated')
ciscoWanAtmConnMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 3)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnChan3MIBGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnStateGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnMIBCompliance3 = ciscoWanAtmConnMIBCompliance3.setStatus('deprecated')
ciscoWanAtmConnMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 4)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnChan4MIBGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmConnStateGroup"), ("CISCO-WAN-ATM-CONN-MIB", "ciscoWanAtmInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnMIBCompliance4 = ciscoWanAtmConnMIBCompliance4.setStatus('current')
ciscoWanAtmConnChanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 1)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDVT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrERS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAisIWCapability"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnChanMIBGroup = ciscoWanAtmConnChanMIBGroup.setStatus('deprecated')
ciscoWanAtmConnStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanAlarmState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanEgressXmtState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanEgressRcvState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIngressXmtState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIngressRcvState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnStateGroup = ciscoWanAtmConnStateGroup.setStatus('current')
ciscoWanAtmConnChan2MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 3)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrERS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAisIWCapability"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnChan2MIBGroup = ciscoWanAtmConnChan2MIBGroup.setStatus('deprecated')
ciscoWanAtmConnChan3MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 4)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSlaveType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingPriority"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnChan3MIBGroup = ciscoWanAtmConnChan3MIBGroup.setStatus('deprecated')
ciscoWanAtmInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 5)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanNumVPCsInAlarm"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanNumVCCsInAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmInformationGroup = ciscoWanAtmInformationGroup.setStatus('current')
ciscoWanAtmConnChan4MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 6)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSlaveType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingPriority"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanP2MP"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPrefRouteId"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanDirectRoute"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"), ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmConnChan4MIBGroup = ciscoWanAtmConnChan4MIBGroup.setStatus('current')
ciscoWanConMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 7)).setObjects(("CISCO-WAN-ATM-CONN-MIB", "cwChanGlobalTransactionId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanConMIBGroup = ciscoWanConMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-MIB", cwaChanRemotePercentUtil=cwaChanRemotePercentUtil, cwaChanTestRoundTripDelay=cwaChanTestRoundTripDelay, ciscoWanAtmConnChan4MIBGroup=ciscoWanAtmConnChan4MIBGroup, cwaChanMBS=cwaChanMBS, cwaChanMCR=cwaChanMCR, cwaChanMaxCost=cwaChanMaxCost, ciscoWanConMIBGroup=ciscoWanConMIBGroup, cwaChanRemoteCTD=cwaChanRemoteCTD, cwAtmChanTestTable=cwAtmChanTestTable, cwaChanRemoteVpi=cwaChanRemoteVpi, cwaChanAbrRIF=cwaChanAbrRIF, cwGlobalChanDataGroup=cwGlobalChanDataGroup, cwaChanNumVCCsInAlarm=cwaChanNumVCCsInAlarm, cwaChanIngressXmtState=cwaChanIngressXmtState, cwaChanPCR=cwaChanPCR, cwaChanAisIWCapability=cwaChanAisIWCapability, PYSNMP_MODULE_ID=ciscoWanAtmConnMIB, cwaChanAbrRDF=cwaChanAbrRDF, cwaChanRemoteMCR=cwaChanRemoteMCR, cwaChanOamSegEpEnable=cwaChanOamSegEpEnable, cwaChanRoutingMastership=cwaChanRoutingMastership, cwaChanAlarmState=cwaChanAlarmState, cwConnMibObjects=cwConnMibObjects, cwaChanDirectRoute=cwaChanDirectRoute, cwaChanLocalVci=cwaChanLocalVci, cwaChanRemoteCLR=cwaChanRemoteCLR, cwaChanVpi=cwaChanVpi, cwaChanSlaveType=cwaChanSlaveType, ciscoWanAtmConnMIBConformance=ciscoWanAtmConnMIBConformance, CiscoWanAisIW=CiscoWanAisIW, CiscoWanLpbkDir=CiscoWanLpbkDir, cwaChanNumVPCsInAlarm=cwaChanNumVPCsInAlarm, cwaChanCDVT=cwaChanCDVT, cwChanGlobalTransactionId=cwChanGlobalTransactionId, CiscoAtmServiceCategory=CiscoAtmServiceCategory, AbrRateFactors=AbrRateFactors, cwaChanEgressRcvState=cwaChanEgressRcvState, cwaChanReroute=cwaChanReroute, cwGlobalChanDataTable=cwGlobalChanDataTable, cwaChanIdentifier=cwaChanIdentifier, cwaChanVci=cwaChanVci, cwaChanRemoteMBS=cwaChanRemoteMBS, cwAtmChanTestEntry=cwAtmChanTestEntry, cwaChanPrefRouteId=cwaChanPrefRouteId, cwaChanVpcFlag=cwaChanVpcFlag, CiscoWanVSVDConfg=CiscoWanVSVDConfg, ciscoWanAtmConnMIBCompliance=ciscoWanAtmConnMIBCompliance, cwaChanIntAbrVSVD=cwaChanIntAbrVSVD, cwAtmChanStateEntry=cwAtmChanStateEntry, cwaChanSCR=cwaChanSCR, cwAtmChanState=cwAtmChanState, cwaChanOperStatus=cwaChanOperStatus, CiscoWanXmtState=CiscoWanXmtState, ciscoWanAtmConnStateGroup=ciscoWanAtmConnStateGroup, cwaChanP2MP=cwaChanP2MP, cwaChanRemotePCR=cwaChanRemotePCR, cwaChanRemoteCDV=cwaChanRemoteCDV, cwaChanRemoteCDVT=cwaChanRemoteCDVT, cwaChanCTD=cwaChanCTD, cwaChanRemoteSCR=cwaChanRemoteSCR, cwaChanAbrTRM=cwaChanAbrTRM, cwaChanRowStatus=cwaChanRowStatus, cwaChanLocalNSAPAddr=cwaChanLocalNSAPAddr, cwaChanCCEnable=cwaChanCCEnable, cwaChanRemoteVci=cwaChanRemoteVci, cwaChanAbrTBE=cwaChanAbrTBE, CiscoWanLpbkTypes=CiscoWanLpbkTypes, cwaChanAbrNRM=cwaChanAbrNRM, CiscoWanRcvState=CiscoWanRcvState, cwaChanLocalVpi=cwaChanLocalVpi, cwaChanTestIterations=cwaChanTestIterations, cwaChanPercentUtil=cwaChanPercentUtil, cwaChanCLR=cwaChanCLR, cwaChanServiceCategory=cwaChanServiceCategory, cwaChanAbrVSVDEnable=cwaChanAbrVSVDEnable, cwAtmChanCnfg=cwAtmChanCnfg, cwaChanFrameDiscard=cwaChanFrameDiscard, ciscoWanAtmConnMIBCompliances=ciscoWanAtmConnMIBCompliances, CiscoWanAlarmState=CiscoWanAlarmState, cwaChanRemoteNSAPAddr=cwaChanRemoteNSAPAddr, cwaChanControllerId=cwaChanControllerId, cwAtmChanCnfgEntry=cwAtmChanCnfgEntry, CiscoWanERSConfg=CiscoWanERSConfg, ciscoWanAtmConnMIBGroups=ciscoWanAtmConnMIBGroups, CiscoWanNsapAtmAddress=CiscoWanNsapAtmAddress, cwaChanAbrCDF=cwaChanAbrCDF, cwaChanStatsEnable=cwaChanStatsEnable, cwAtmChanCnfgTable=cwAtmChanCnfgTable, cwaChanAbrERS=cwaChanAbrERS, cwaChanIngressRcvState=cwaChanIngressRcvState, cwAtmChanStateTable=cwAtmChanStateTable, cwAtmChanInformation=cwAtmChanInformation, cwaChanRoutingPriority=cwaChanRoutingPriority, cwaChanAbrICR=cwaChanAbrICR, ciscoWanAtmConnChan2MIBGroup=ciscoWanAtmConnChan2MIBGroup, cwaChanCDV=cwaChanCDV, ciscoWanAtmConnMIBCompliance3=ciscoWanAtmConnMIBCompliance3, CiscoWanTestStatus=CiscoWanTestStatus, cwaChanTestState=cwaChanTestState, cwaChanExtAbrVSVD=cwaChanExtAbrVSVD, cwaChanAbrADTF=cwaChanAbrADTF, cwGlobalChanDataEntry=cwGlobalChanDataEntry, cwAtmChanTest=cwAtmChanTest, cwaChanTestDir=cwaChanTestDir, ciscoWanAtmConnMIBCompliance4=ciscoWanAtmConnMIBCompliance4, CiscoWanOperStatus=CiscoWanOperStatus, cwaChanUploadCounter=cwaChanUploadCounter, ciscoWanAtmConnMIB=ciscoWanAtmConnMIB, ciscoWanAtmConnMIBCompliance2=ciscoWanAtmConnMIBCompliance2, ciscoWanAtmConnChan3MIBGroup=ciscoWanAtmConnChan3MIBGroup, cwaChanTestType=cwaChanTestType, ciscoWanAtmInformationGroup=ciscoWanAtmInformationGroup, cwaChanEgressXmtState=cwaChanEgressXmtState, cwaChanAbrFRTT=cwaChanAbrFRTT, ciscoWanAtmConnChanMIBGroup=ciscoWanAtmConnChanMIBGroup, cwSlotIndex=cwSlotIndex)

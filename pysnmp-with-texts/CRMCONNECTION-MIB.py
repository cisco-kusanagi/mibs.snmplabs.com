#
# PySNMP MIB module CRMCONNECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CRMCONNECTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
atmVplVpi, atmVclVci, atmTrafficDescrParamIndex, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVplVpi", "atmVclVci", "atmTrafficDescrParamIndex", "atmVclVpi")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, Counter32, TimeTicks, iso, NotificationType, Counter64, Gauge32, MibIdentifier, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Counter32", "TimeTicks", "iso", "NotificationType", "Counter64", "Gauge32", "MibIdentifier", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32", "Bits")
DisplayString, TextualConvention, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "RowStatus")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
ntt = MibIdentifier((1, 3, 6, 1, 4, 1, 210))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 210, 2))
ba3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 210, 2, 8))
crmCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 210, 2, 8, 1))
crmConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1))
crmTrPrmTable = MibTable((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: crmTrPrmTable.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmTable.setDescription('DUMMY')
crmTrPrmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "CRMCONNECTION-MIB", "crmTrPrmIndex"))
if mibBuilder.loadTexts: crmTrPrmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmEntry.setDescription('DUMMY')
crmTrPrmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647)))
if mibBuilder.loadTexts: crmTrPrmIndex.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmIndex.setDescription('DUMMY')
crmTrPrmCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 2), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmCategory.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmCategory.setDescription('DUMMY')
crmTrPrmCDVT = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647)).clone(720)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmCDVT.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmCDVT.setDescription('DUMMY')
crmTrPrmCellDelayPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 4), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmCellDelayPriority.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmCellDelayPriority.setDescription('DUMMY')
crmTrPrmCellLossPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 5), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmCellLossPriority.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmCellLossPriority.setDescription('DUMMY')
crmTrPrmUPCInfo1 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 6), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmUPCInfo1.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmUPCInfo1.setDescription('DUMMY')
crmTrPrmUPCInfo2 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmUPCInfo2.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmUPCInfo2.setDescription('DUMMY')
crmTrPrmUPCInfo3 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmUPCInfo3.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmUPCInfo3.setDescription('DUMMY')
crmTrPrmUPCInfo4 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmUPCInfo4.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmUPCInfo4.setDescription('DUMMY')
crmTrPrmShapingInfo1 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 10), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmShapingInfo1.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmShapingInfo1.setDescription('DUMMY')
crmTrPrmShapingInfo2 = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmShapingInfo2.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmShapingInfo2.setDescription('DUMMY')
crmTrPrmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmRowStatus.setDescription('DUMMY')
crmTrPrmEpdPpd = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("epdppdoff", 1), ("ppdon", 2), ("epdppdon", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmEpdPpd.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmEpdPpd.setDescription('DUMMY')
crmTrPrmHeavyCongestionTh = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 14), Integer32().clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmHeavyCongestionTh.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmHeavyCongestionTh.setDescription('DUMMY')
crmTrPrmLightCongestionTh = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 15), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmLightCongestionTh.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmLightCongestionTh.setDescription('DUMMY')
crmTrPrmEFCIMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmEFCIMarking.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmEFCIMarking.setDescription('DUMMY')
crmTrPrmNICIMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmNICIMarking.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmNICIMarking.setDescription('DUMMY')
crmTrPrmERMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmERMarking.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmERMarking.setDescription('DUMMY')
crmTrPrmBECNCellSending = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmBECNCellSending.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmBECNCellSending.setDescription('DUMMY')
crmTrPrmVSVD = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmVSVD.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmVSVD.setDescription('DUMMY')
crmTrPrmRDF = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 21), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmRDF.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmRDF.setDescription('DUMMY')
crmTrPrmRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 22), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmRIF.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmRIF.setDescription('DUMMY')
crmTrPrmCDF = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 23), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmTrPrmCDF.setStatus('mandatory')
if mibBuilder.loadTexts: crmTrPrmCDF.setDescription('DUMMY')
crmVplXtndTable = MibTable((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: crmVplXtndTable.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplXtndTable.setDescription('DUMMY')
crmVplXtndEntry = MibTableRow((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVplVpi"))
if mibBuilder.loadTexts: crmVplXtndEntry.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplXtndEntry.setDescription('DUMMY')
crmVplGenCastType = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVplGenCastType.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplGenCastType.setDescription('DUMMY')
crmVplLogicalPortDef = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVplLogicalPortDef.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplLogicalPortDef.setDescription('DUMMY')
crmVplLogicalPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crmVplLogicalPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplLogicalPortIndex.setDescription('DUMMY')
crmVplRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVplRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: crmVplRowStatus.setDescription('DUMMY')
crmVclXtndTable = MibTable((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3), )
if mibBuilder.loadTexts: crmVclXtndTable.setStatus('mandatory')
if mibBuilder.loadTexts: crmVclXtndTable.setDescription('DUMMY')
crmVclXtndEntry = MibTableRow((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: crmVclXtndEntry.setStatus('mandatory')
if mibBuilder.loadTexts: crmVclXtndEntry.setDescription('DUMMY')
crmVclGenConType = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVclGenConType.setStatus('mandatory')
if mibBuilder.loadTexts: crmVclGenConType.setDescription('DUMMY')
crmVclGenCastType = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVclGenCastType.setStatus('mandatory')
if mibBuilder.loadTexts: crmVclGenCastType.setDescription('DUMMY')
crmVclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: crmVclRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: crmVclRowStatus.setDescription('DUMMY')
mibBuilder.exportSymbols("CRMCONNECTION-MIB", org=org, crmTrPrmCellLossPriority=crmTrPrmCellLossPriority, crmVplLogicalPortIndex=crmVplLogicalPortIndex, crmTrPrmUPCInfo4=crmTrPrmUPCInfo4, crmTrPrmNICIMarking=crmTrPrmNICIMarking, crmVplXtndEntry=crmVplXtndEntry, enterprises=enterprises, crmTrPrmShapingInfo2=crmTrPrmShapingInfo2, ba3000=ba3000, crmTrPrmVSVD=crmTrPrmVSVD, crmTrPrmLightCongestionTh=crmTrPrmLightCongestionTh, crmCommon=crmCommon, crmTrPrmEntry=crmTrPrmEntry, crmTrPrmBECNCellSending=crmTrPrmBECNCellSending, crmTrPrmEpdPpd=crmTrPrmEpdPpd, crmTrPrmRowStatus=crmTrPrmRowStatus, crmTrPrmCategory=crmTrPrmCategory, crmVclGenConType=crmVclGenConType, crmTrPrmUPCInfo3=crmTrPrmUPCInfo3, crmVclXtndTable=crmVclXtndTable, dod=dod, private=private, crmVclRowStatus=crmVclRowStatus, mibDoc=mibDoc, ntt=ntt, crmTrPrmUPCInfo2=crmTrPrmUPCInfo2, internet=internet, crmConnection=crmConnection, crmTrPrmHeavyCongestionTh=crmTrPrmHeavyCongestionTh, crmVplXtndTable=crmVplXtndTable, crmTrPrmERMarking=crmTrPrmERMarking, crmTrPrmUPCInfo1=crmTrPrmUPCInfo1, crmTrPrmEFCIMarking=crmTrPrmEFCIMarking, crmTrPrmTable=crmTrPrmTable, crmTrPrmRIF=crmTrPrmRIF, crmTrPrmCDF=crmTrPrmCDF, crmVplGenCastType=crmVplGenCastType, crmTrPrmCDVT=crmTrPrmCDVT, crmTrPrmCellDelayPriority=crmTrPrmCellDelayPriority, crmVplRowStatus=crmVplRowStatus, crmTrPrmRDF=crmTrPrmRDF, crmTrPrmShapingInfo1=crmTrPrmShapingInfo1, crmVclGenCastType=crmVclGenCastType, crmVclXtndEntry=crmVclXtndEntry, crmVplLogicalPortDef=crmVplLogicalPortDef, crmTrPrmIndex=crmTrPrmIndex)

#
# PySNMP MIB module SUN-HW-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-HW-CTRL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, Gauge32, Counter32, Bits, IpAddress, Unsigned32, MibIdentifier, NotificationType, Counter64, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Gauge32", "Counter32", "Bits", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Counter64", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks")
TruthValue, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "DateAndTime")
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
ilom = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175))
sunHwCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 175, 104))
sunHwCtrlMIB.setRevisions(('2010-01-04 00:00', '2009-08-20 00:00', '2009-07-28 00:00', '2009-03-01 00:00', '2008-09-01 00:00',))
if mibBuilder.loadTexts: sunHwCtrlMIB.setLastUpdated('201001040000Z')
if mibBuilder.loadTexts: sunHwCtrlMIB.setOrganization('Sun Microsystems, Inc.')
sunHwCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1))
sunHwCtrlMIBConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2))
sunHwCtrlPowerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6))
sunHwCtrlTPM = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7))
sunHwCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 1))
sunHwCtrlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2))
class SunHwCtrlPowerMgmtID(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SunHwCtrlPowerMgmtPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notsupported", 1), ("unknown", 2), ("performance", 3), ("elastic", 4))

class SunHwCtrlPowerMgmtBudgetTimelimitActions(TextualConvention, Bits):
    reference = 'Data Center Management Interface (DCMI) version 1.0, 5/2008.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("hardPowerOff", 1))

sunHwCtrlReservedPSU = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlReservedPSU.setStatus('current')
sunHwCtrlTotalPSU = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlTotalPSU.setStatus('current')
sunHwCtrlPowerMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3), )
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtTable.setStatus('current')
sunHwCtrlPowerMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1), ).setIndexNames((0, "SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtID"))
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtEntry.setStatus('current')
sunHwCtrlPowerMgmtID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 1), SunHwCtrlPowerMgmtID())
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtID.setStatus('current')
sunHwCtrlPowerMgmtName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtName.setStatus('current')
sunHwCtrlPowerMgmtUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtUnits.setStatus('current')
sunHwCtrlPowerMgmtValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtValue.setStatus('current')
sunHwCtrlPowerMgmtActualPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtActualPower.setStatus('current')
sunHwCtrlPowerMgmtPermittedPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPermittedPower.setStatus('current')
sunHwCtrlPowerMgmtAvailablePower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtAvailablePower.setStatus('current')
sunHwCtrlPowerMgmtPolicy = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 7), SunHwCtrlPowerMgmtPolicy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPolicy.setStatus('current')
sunHwCtrlPowerMgmtBudgetSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9))
sunHwCtrlPowerMgmtBudget = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("enabledPostPoweron", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudget.setStatus('current')
sunHwCtrlPowerMgmtBudgetMinPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetMinPowerlimit.setStatus('current')
sunHwCtrlPowerMgmtBudgetPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPowerlimit.setStatus('current')
sunHwCtrlPowerMgmtBudgetTimelimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimit.setStatus('current')
sunHwCtrlPowerMgmtBudgetTimelimitActions = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 6), SunHwCtrlPowerMgmtBudgetTimelimitActions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimitActions.setStatus('current')
sunHwCtrlPowerMgmtBudgetOK = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetOK.setStatus('current')
sunHwCtrlPowerMgmtBudgetCommitPending = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 100), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetCommitPending.setStatus('current')
sunHwCtrlPowerMgmtBudgetPendingPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 103), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setStatus('current')
sunHwCtrlPowerMgmtBudgetPendingTimelimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 105), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimit.setStatus('current')
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 106), SunHwCtrlPowerMgmtBudgetTimelimitActions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setStatus('current')
sunHwCtrlPowerMgmtConsumptionThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10))
sunHwCtrlPowerMgmtConsumptionThreshold1 = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold1.setStatus('current')
sunHwCtrlPowerMgmtConsumptionThreshold2 = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold2.setStatus('current')
sunHwCtrlPowerMgmtSampling = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11))
sunHwCtrlPowerMgmtSamplingPeriod = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingPeriod.setStatus('current')
sunHwCtrlPowerMgmtSamplingTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingTimestamp.setStatus('current')
sunHwCtrlPowerMgmtSamplingMinimumPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMinimumPower.setStatus('current')
sunHwCtrlPowerMgmtSamplingMaximumPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMaximumPower.setStatus('current')
sunHwCtrlPowerMgmtSamplingAveragePower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingAveragePower.setStatus('current')
sunHwCtrlTpmEnable = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmEnable.setStatus('current')
sunHwCtrlTpmActivate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmActivate.setStatus('current')
sunHwCtrlTpmForceClear = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmForceClear.setStatus('current')
sunHwCtrlObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2, 1)).setObjects(("SUN-HW-CTRL-MIB", "sunHwCtrlReservedPSU"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTotalPSU"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtName"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtUnits"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtValue"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtActualPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPermittedPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtAvailablePower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPolicy"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudget"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetMinPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimitActions"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetOK"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetCommitPending"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimitActions"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold1"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold2"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingPeriod"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingTimestamp"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMinimumPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMaximumPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingAveragePower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmEnable"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmActivate"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmForceClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunHwCtrlObjectsGroup = sunHwCtrlObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("SUN-HW-CTRL-MIB", sunHwCtrlTpmActivate=sunHwCtrlTpmActivate, sunHwCtrlPowerMgmtTable=sunHwCtrlPowerMgmtTable, sunHwCtrlPowerMgmtEntry=sunHwCtrlPowerMgmtEntry, sunHwCtrlPowerMgmtValue=sunHwCtrlPowerMgmtValue, ilom=ilom, sunHwCtrlPowerMgmt=sunHwCtrlPowerMgmt, SunHwCtrlPowerMgmtID=SunHwCtrlPowerMgmtID, sunHwCtrlPowerMgmtBudgetPendingTimelimit=sunHwCtrlPowerMgmtBudgetPendingTimelimit, sunHwCtrlPowerMgmtBudget=sunHwCtrlPowerMgmtBudget, sunHwCtrlPowerMgmtBudgetMinPowerlimit=sunHwCtrlPowerMgmtBudgetMinPowerlimit, sunHwCtrlPowerMgmtBudgetTimelimitActions=sunHwCtrlPowerMgmtBudgetTimelimitActions, sunHwCtrlPowerMgmtSampling=sunHwCtrlPowerMgmtSampling, sunHwCtrlReservedPSU=sunHwCtrlReservedPSU, sunHwCtrlPowerMgmtSamplingPeriod=sunHwCtrlPowerMgmtSamplingPeriod, sunHwCtrlPowerMgmtActualPower=sunHwCtrlPowerMgmtActualPower, sunHwCtrlPowerMgmtBudgetCommitPending=sunHwCtrlPowerMgmtBudgetCommitPending, sunHwCtrlPowerMgmtConsumptionThresholds=sunHwCtrlPowerMgmtConsumptionThresholds, SunHwCtrlPowerMgmtBudgetTimelimitActions=SunHwCtrlPowerMgmtBudgetTimelimitActions, sunHwCtrlPowerMgmtSamplingMinimumPower=sunHwCtrlPowerMgmtSamplingMinimumPower, sunHwCtrlMIB=sunHwCtrlMIB, sunHwCtrlPowerMgmtUnits=sunHwCtrlPowerMgmtUnits, SunHwCtrlPowerMgmtPolicy=SunHwCtrlPowerMgmtPolicy, sunHwCtrlPowerMgmtBudgetSettings=sunHwCtrlPowerMgmtBudgetSettings, sunHwCtrlPowerMgmtAvailablePower=sunHwCtrlPowerMgmtAvailablePower, sunHwCtrlTpmEnable=sunHwCtrlTpmEnable, products=products, sunHwCtrlCompliances=sunHwCtrlCompliances, sunHwCtrlPowerMgmtID=sunHwCtrlPowerMgmtID, sunHwCtrlPowerMgmtBudgetPendingTimelimitActions=sunHwCtrlPowerMgmtBudgetPendingTimelimitActions, sunHwCtrlPowerMgmtConsumptionThreshold2=sunHwCtrlPowerMgmtConsumptionThreshold2, sunHwCtrlMIBConformances=sunHwCtrlMIBConformances, sunHwCtrlPowerMgmtBudgetTimelimit=sunHwCtrlPowerMgmtBudgetTimelimit, sunHwCtrlGroups=sunHwCtrlGroups, PYSNMP_MODULE_ID=sunHwCtrlMIB, sunHwCtrlTpmForceClear=sunHwCtrlTpmForceClear, sunHwCtrlPowerMgmtBudgetPowerlimit=sunHwCtrlPowerMgmtBudgetPowerlimit, sunHwCtrlTPM=sunHwCtrlTPM, sunHwCtrlTotalPSU=sunHwCtrlTotalPSU, sunHwCtrlPowerMgmtConsumptionThreshold1=sunHwCtrlPowerMgmtConsumptionThreshold1, sunHwCtrlPowerMgmtSamplingTimestamp=sunHwCtrlPowerMgmtSamplingTimestamp, sun=sun, sunHwCtrlPowerMgmtPolicy=sunHwCtrlPowerMgmtPolicy, sunHwCtrlPowerMgmtSamplingAveragePower=sunHwCtrlPowerMgmtSamplingAveragePower, sunHwCtrlObjectsGroup=sunHwCtrlObjectsGroup, sunHwCtrlMIBObjects=sunHwCtrlMIBObjects, sunHwCtrlPowerMgmtName=sunHwCtrlPowerMgmtName, sunHwCtrlPowerMgmtPermittedPower=sunHwCtrlPowerMgmtPermittedPower, sunHwCtrlPowerMgmtBudgetPendingPowerlimit=sunHwCtrlPowerMgmtBudgetPendingPowerlimit, sunHwCtrlPowerMgmtBudgetOK=sunHwCtrlPowerMgmtBudgetOK, sunHwCtrlPowerMgmtSamplingMaximumPower=sunHwCtrlPowerMgmtSamplingMaximumPower)

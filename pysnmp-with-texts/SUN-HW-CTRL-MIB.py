#
# PySNMP MIB module SUN-HW-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-HW-CTRL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Unsigned32, Counter64, IpAddress, iso, TimeTicks, ModuleIdentity, enterprises, Gauge32, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "IpAddress", "iso", "TimeTicks", "ModuleIdentity", "enterprises", "Gauge32", "Bits", "Integer32", "ObjectIdentity")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
ilom = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175))
sunHwCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 175, 104))
sunHwCtrlMIB.setRevisions(('2010-01-04 00:00', '2009-08-20 00:00', '2009-07-28 00:00', '2009-03-01 00:00', '2008-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sunHwCtrlMIB.setRevisionsDescriptions(('Modified handling of TPM parameters.', 'Add TPM parameters.', 'Version: 1.0 Release versioning only', 'Version: 0.2 Added: sunHwCtrlPowerMgmtBudgetSettings sunHwCtrlPowerMgmtConsumptionThresholds sunHwCtrlPowerMgmtSampling', 'Version: 0.1 Initial Release',))
if mibBuilder.loadTexts: sunHwCtrlMIB.setLastUpdated('201001040000Z')
if mibBuilder.loadTexts: sunHwCtrlMIB.setOrganization('Sun Microsystems, Inc.')
if mibBuilder.loadTexts: sunHwCtrlMIB.setContactInfo('Sun Microsystems, Inc 4150 Network Circle Santa Clara, CA 95054 1-800-555-9SUN or 1-650-960-1300 http://www.sun.com')
if mibBuilder.loadTexts: sunHwCtrlMIB.setDescription('SUN-HW-CTRL-MIB.mib Version 1.1 Copyright 2010, by Sun Microsystems, Inc. All rights reserved. Use is subject to license terms. This MIB allows controls for all Sun platform devices using Integrated Lights Out Management.')
sunHwCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1))
sunHwCtrlMIBConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2))
sunHwCtrlPowerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6))
sunHwCtrlTPM = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7))
sunHwCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 1))
sunHwCtrlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2))
class SunHwCtrlPowerMgmtID(TextualConvention, Integer32):
    description = 'An arbitrary value which uniquely identifies the power management table index. The value should be a small positive integer; index values for different policy entities are not necessarily contiguous.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SunHwCtrlPowerMgmtPolicy(TextualConvention, Integer32):
    description = 'An enumerated value which describes the defined power management policies available. A value of notsupported(1) indicates that the control is not available on the managed platform. A value of unknown(2) indicates that the control is available, but the current state can not be determined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notsupported", 1), ("unknown", 2), ("performance", 3), ("elastic", 4))

class SunHwCtrlPowerMgmtBudgetTimelimitActions(TextualConvention, Bits):
    reference = 'Data Center Management Interface (DCMI) version 1.0, 5/2008.'
    description = 'The list of actions that will occur if the power limit is exceeded and cannot be controlled within the time limits SunHwCtrlPowerMgmtBudgetTimelimit'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("hardPowerOff", 1))

sunHwCtrlReservedPSU = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlReservedPSU.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlReservedPSU.setDescription("The number of Reserved PSU's.")
sunHwCtrlTotalPSU = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlTotalPSU.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlTotalPSU.setDescription("The total number of PSU's.")
sunHwCtrlPowerMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3), )
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtTable.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtTable.setDescription('A table listing additional power management properties.')
sunHwCtrlPowerMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1), ).setIndexNames((0, "SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtID"))
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtEntry.setDescription('An entry for a power management property.')
sunHwCtrlPowerMgmtID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 1), SunHwCtrlPowerMgmtID())
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtID.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtID.setDescription('This is an index for the sunHwCtrlPowerMgmtTable.')
sunHwCtrlPowerMgmtName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtName.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtName.setDescription('This is the name of the power management property.')
sunHwCtrlPowerMgmtUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtUnits.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtUnits.setDescription('This is the units for the value of the power management property.')
sunHwCtrlPowerMgmtValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtValue.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtValue.setDescription('This is the value of the power management property.')
sunHwCtrlPowerMgmtActualPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtActualPower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtActualPower.setDescription('Total input power consumed in watts. On a rackmount server, total power consumption is the input power consumed by the server. On a blade, this is the input power consumed just by the blade (not including any power consumed by shared components). On a CMM this is the input power consumed by the entire chassis or shelf, all blades, NEMs, fans, etc.')
sunHwCtrlPowerMgmtPermittedPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPermittedPower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPermittedPower.setDescription("Maximum input power consumption in watts. On a rackmount server, the maximum power consumption is the maximum input power the server guarantees it will consume at any instant. On a blade, this is the maximum input power a blade guarantees it will consume, not including its power load on shared components. On a CMM this is the maximum input power the entire chassis (all blades, NEMs, fans, etc.) will consume at any instant. This value can't be changed directly, but may change based on the power policy and budget, and chassis power capacity.")
sunHwCtrlPowerMgmtAvailablePower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtAvailablePower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtAvailablePower.setDescription('Maximum input power capacity in watts. Power capacity is the maximum input power the power supplies are capable of consuming. On a blade, this is the amount of power guaranteed available to the blade by the chassis.')
sunHwCtrlPowerMgmtPolicy = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 7), SunHwCtrlPowerMgmtPolicy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPolicy.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtPolicy.setDescription('Indicates the desired power managment policy.')
sunHwCtrlPowerMgmtBudgetSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9))
sunHwCtrlPowerMgmtBudget = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("enabledPostPoweron", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudget.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudget.setDescription('When reading, the current state of the following budget settings: sunHwCtrlPowerMgmtBudgetMinPowerlimit sunHwCtrlPowerMgmtBudgetPowerlimit sunHwCtrlPowerMgmtBudgetTimelimit sunHwCtrlPowerMgmtBudgetTimelimitActions If unknown(1), the agent could not determine the current state. If disabled(2), the settings are not currently in effect. If enabled(3), the settings are currently in effect. If enabledPostPoweron(4), the settings will take effect after the processor is powered on. When writing, only disabled(2) and enabled(3) are valid values. If set to enabled(3) while the system if powered off, the budget will not be enforced until the system powers on and this will transition to enabledPostPoweron(4). If set to enabled(3) when the current budget settings are not supported, this will transition to disabled(2).')
sunHwCtrlPowerMgmtBudgetMinPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetMinPowerlimit.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetMinPowerlimit.setDescription('Minimum value sunHwCtrlPowerMgmtBudgetPowerlimit can be set to. The power capper can control power consumption to fit within as little as this amount of power when the system is powered on.')
sunHwCtrlPowerMgmtBudgetPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPowerlimit.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPowerlimit.setDescription('Maximum power consumption in watts.')
sunHwCtrlPowerMgmtBudgetTimelimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimit.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimit.setDescription('Grace period for exceeding the powerlimit once the powerlimit has been achieved, in milliseconds.')
sunHwCtrlPowerMgmtBudgetTimelimitActions = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 6), SunHwCtrlPowerMgmtBudgetTimelimitActions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimitActions.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetTimelimitActions.setDescription('List of actions that will occur if the power limit is exceeded and cannot be controlled within the timelimit. hardpoweroff(1) causes a hard power off if the timelimit is exceeded.')
sunHwCtrlPowerMgmtBudgetOK = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetOK.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetOK.setDescription("'true' if sunHwCtrlPowerMgmtBudget is 'disabled(2)'. If sunHwCtrlPowerMgmtBudget is 'enabled(3)', sunHwCtrlPowerMgmtBudgetOK will be 'false' if the power consumption has been over the power limit (sunHwCtrlPowerMgmtBudgetPowerlimit) for more than the time limit (sunHwCtrlPowerMgmtBudgetTimelimit), otherwise 'true'. Returns to 'true' when power consumption drops to or below the powerlimit after a violation. This value will also be 'false' if the budget is enabled but the budget settings are not supported. (This could happen if saved budget settings are no longer valid after a reboot.)")
sunHwCtrlPowerMgmtBudgetCommitPending = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 100), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetCommitPending.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetCommitPending.setDescription('Commits the following pending values: sunHwCtrlPowerMgmtBudgetPendingPowerlimit sunHwCtrlPowerMgmtBudgetPendingTimelimit sunHwCtrlPowerMgmtBudgetPendingTimelimitActions May only be set to true.')
sunHwCtrlPowerMgmtBudgetPendingPowerlimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 103), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setDescription('When committed, the value is applied to sunHwCtrlPowerMgmtBudgetPowerlimit.')
sunHwCtrlPowerMgmtBudgetPendingTimelimit = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 105), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimit.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimit.setDescription("When committed, the value is applied to sunHwCtrlPowerMgmtBudgetTimelimit. A value of -1 instructs the system to use its' default value.")
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 106), SunHwCtrlPowerMgmtBudgetTimelimitActions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setDescription('When committed, the value is applied to sunHwCtrlPowerMgmtBudgetTimelimitActions.')
sunHwCtrlPowerMgmtConsumptionThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10))
sunHwCtrlPowerMgmtConsumptionThreshold1 = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold1.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold1.setDescription('A threshold that determines if ILOM threshold events get generated based on the value of the system power consumption sensor (typically /SYS/VPS). Valid values are 0 (zero) when disabled; greater than 0 generates threshold crossing event.')
sunHwCtrlPowerMgmtConsumptionThreshold2 = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setUnits('watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold2.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtConsumptionThreshold2.setDescription('A threshold that determines if ILOM threshold events get generated based on the value of the system power consumption sensor (typically /SYS/VPS). Valid values are 0 (zero) when disabled; greater than 0 generates threshold crossing event.')
sunHwCtrlPowerMgmtSampling = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11))
sunHwCtrlPowerMgmtSamplingPeriod = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingPeriod.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingPeriod.setDescription('Sampling period over which sunHwCtrlPowerMgmtSamplingMinimumPower, sunHwCtrlPowerMgmtSamplingMaximumPower and sunHwCtrlPowerMgmtSamplingAveragePower are calculated and reported, in seconds. Supported range and granularity are platform specific.')
sunHwCtrlPowerMgmtSamplingTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingTimestamp.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingTimestamp.setDescription('Date and time at which the power consumption values were calculated.')
sunHwCtrlPowerMgmtSamplingMinimumPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMinimumPower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMinimumPower.setDescription('Minimum measured power consumption during most recent sampling period, in watts')
sunHwCtrlPowerMgmtSamplingMaximumPower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMaximumPower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingMaximumPower.setDescription('Maximum measured power consumption during most recent sampling period, in watts')
sunHwCtrlPowerMgmtSamplingAveragePower = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingAveragePower.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlPowerMgmtSamplingAveragePower.setDescription('Average measured power consumption during most recent sampling period, in watts')
sunHwCtrlTpmEnable = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmEnable.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlTpmEnable.setDescription('sunHwCtrlTpmEnable is the principal control for any action being taken to change the access mode(s) of the TPM device. Any attempt to change sunHwCtrlTpmEnable when the host power is on will generate an inconsistentValue (or badValue for SNMPv1) error. When sunHwCtrlTpmEnable is set to false(2), no changes to sunHwCtrlTpmActivate will succeed, and the TPM device will be disabled during the next host power on event. If sunHwCtrlTpmEnable is set to true(1), the TPM device will be enabled during the next host power on. The default state of sunHwCtrlTpmEnable is false(2).')
sunHwCtrlTpmActivate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmActivate.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlTpmActivate.setDescription('If sunHwCtrlTpmActivate and sunHwCtrlTpmEnable are both currently true(1) during a host power on event, the TPM device will be enabled and activated. If sunHwCtrlTpmActivate is currently false(2) and sunHwCtrlTpmEnable is currently true(1) during a host power on event, the TPM device will be enabled and deactivated. When sunHwCtrlTpmEnable is set to false(2), no changes to sunHwCtrlTpmActivate will succeed. The default state of sunHwCtrlTpmActivate is false(2).')
sunHwCtrlTpmForceClear = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunHwCtrlTpmForceClear.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlTpmForceClear.setDescription('If sunHwCtrlTpmForceClear and sunHwCtrlTpmEnable are both currently true(1) during a host power on event, the TPM device state will be purged and the state of sunHwCtrlTpmForceClear will return to false(2). If sunHwCtrlTpmForceClear is currently true(1) and sunHwCtrlTpmEnable is currently false(2) during a host power on event, the TPM device will not be enabled, no action is taken with regard to the state of the TPM device, and sunHwCtrlTpmForceClear remains true(1). If sunHwCtrlTpmForceClear is currently false(2) and sunHwCtrlTpmEnable is currently true(1) during a host power on event, the TPM device will be enabled, no action is taken with regard to the state of the TPM device, and sunHwCtrlTpmForceClear remains false(2). When sunHwCtrlTpmEnable is set to false(2), no changes to sunHwCtrlTpmForceClear will succeed.')
sunHwCtrlObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2, 1)).setObjects(("SUN-HW-CTRL-MIB", "sunHwCtrlReservedPSU"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTotalPSU"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtName"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtUnits"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtValue"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtActualPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPermittedPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtAvailablePower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPolicy"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudget"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetMinPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimitActions"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetOK"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetCommitPending"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingPowerlimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimit"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimitActions"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold1"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold2"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingPeriod"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingTimestamp"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMinimumPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMaximumPower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingAveragePower"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmEnable"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmActivate"), ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmForceClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunHwCtrlObjectsGroup = sunHwCtrlObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: sunHwCtrlObjectsGroup.setDescription('The group of current objects.')
mibBuilder.exportSymbols("SUN-HW-CTRL-MIB", sunHwCtrlPowerMgmtID=sunHwCtrlPowerMgmtID, sunHwCtrlMIBObjects=sunHwCtrlMIBObjects, sunHwCtrlPowerMgmtUnits=sunHwCtrlPowerMgmtUnits, sunHwCtrlGroups=sunHwCtrlGroups, sunHwCtrlPowerMgmtBudgetOK=sunHwCtrlPowerMgmtBudgetOK, sunHwCtrlPowerMgmtSamplingAveragePower=sunHwCtrlPowerMgmtSamplingAveragePower, sunHwCtrlPowerMgmtPermittedPower=sunHwCtrlPowerMgmtPermittedPower, sunHwCtrlPowerMgmtBudgetPendingPowerlimit=sunHwCtrlPowerMgmtBudgetPendingPowerlimit, sunHwCtrlPowerMgmtName=sunHwCtrlPowerMgmtName, SunHwCtrlPowerMgmtID=SunHwCtrlPowerMgmtID, sunHwCtrlPowerMgmtTable=sunHwCtrlPowerMgmtTable, PYSNMP_MODULE_ID=sunHwCtrlMIB, sunHwCtrlTpmActivate=sunHwCtrlTpmActivate, sunHwCtrlPowerMgmt=sunHwCtrlPowerMgmt, sunHwCtrlPowerMgmtBudgetTimelimit=sunHwCtrlPowerMgmtBudgetTimelimit, sunHwCtrlPowerMgmtBudgetPendingTimelimitActions=sunHwCtrlPowerMgmtBudgetPendingTimelimitActions, ilom=ilom, sunHwCtrlPowerMgmtSamplingPeriod=sunHwCtrlPowerMgmtSamplingPeriod, sunHwCtrlPowerMgmtBudgetMinPowerlimit=sunHwCtrlPowerMgmtBudgetMinPowerlimit, sunHwCtrlPowerMgmtConsumptionThreshold2=sunHwCtrlPowerMgmtConsumptionThreshold2, sunHwCtrlPowerMgmtBudgetPowerlimit=sunHwCtrlPowerMgmtBudgetPowerlimit, sunHwCtrlPowerMgmtBudgetSettings=sunHwCtrlPowerMgmtBudgetSettings, sunHwCtrlTpmEnable=sunHwCtrlTpmEnable, sunHwCtrlMIB=sunHwCtrlMIB, products=products, sunHwCtrlPowerMgmtSampling=sunHwCtrlPowerMgmtSampling, sunHwCtrlTotalPSU=sunHwCtrlTotalPSU, sunHwCtrlPowerMgmtValue=sunHwCtrlPowerMgmtValue, sunHwCtrlPowerMgmtSamplingMinimumPower=sunHwCtrlPowerMgmtSamplingMinimumPower, sunHwCtrlPowerMgmtConsumptionThreshold1=sunHwCtrlPowerMgmtConsumptionThreshold1, SunHwCtrlPowerMgmtPolicy=SunHwCtrlPowerMgmtPolicy, sunHwCtrlCompliances=sunHwCtrlCompliances, sunHwCtrlPowerMgmtEntry=sunHwCtrlPowerMgmtEntry, sunHwCtrlPowerMgmtBudgetCommitPending=sunHwCtrlPowerMgmtBudgetCommitPending, sunHwCtrlPowerMgmtPolicy=sunHwCtrlPowerMgmtPolicy, sunHwCtrlReservedPSU=sunHwCtrlReservedPSU, sunHwCtrlPowerMgmtConsumptionThresholds=sunHwCtrlPowerMgmtConsumptionThresholds, sun=sun, sunHwCtrlPowerMgmtAvailablePower=sunHwCtrlPowerMgmtAvailablePower, sunHwCtrlPowerMgmtBudget=sunHwCtrlPowerMgmtBudget, sunHwCtrlObjectsGroup=sunHwCtrlObjectsGroup, sunHwCtrlPowerMgmtSamplingMaximumPower=sunHwCtrlPowerMgmtSamplingMaximumPower, sunHwCtrlTPM=sunHwCtrlTPM, SunHwCtrlPowerMgmtBudgetTimelimitActions=SunHwCtrlPowerMgmtBudgetTimelimitActions, sunHwCtrlPowerMgmtBudgetTimelimitActions=sunHwCtrlPowerMgmtBudgetTimelimitActions, sunHwCtrlPowerMgmtSamplingTimestamp=sunHwCtrlPowerMgmtSamplingTimestamp, sunHwCtrlPowerMgmtBudgetPendingTimelimit=sunHwCtrlPowerMgmtBudgetPendingTimelimit, sunHwCtrlTpmForceClear=sunHwCtrlTpmForceClear, sunHwCtrlPowerMgmtActualPower=sunHwCtrlPowerMgmtActualPower, sunHwCtrlMIBConformances=sunHwCtrlMIBConformances)

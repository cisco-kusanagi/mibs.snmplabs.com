#
# PySNMP MIB module SYMMCOMMONDTI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONDTI
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:49 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, TimeTicks, NotificationType, iso, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "TimeTicks", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmDti = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7))
if mibBuilder.loadTexts: symmDti.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: symmDti.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmDti.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmDti.setDescription('Symmetricom, Inc. Common DTI status and configuration ')
class EnaValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class TPModuleID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("sys", 1), ("imc", 2), ("ioc1", 3), ("ioc2", 4), ("exp0", 5), ("exp1", 6), ("exp2", 7), ("exp3", 8), ("exp4", 9), ("exp5", 10), ("exp6", 11), ("exp7", 12), ("exp8", 13), ("exp9", 14))

class OnValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class ActionApply(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("apply", 1), ("nonapply", 2))

class OpMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

class ActiveValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class YesValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class OkValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fault", 2))

class ValidValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valid", 1), ("invalid", 2), ("nurture", 3))

class TableRowChange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("add", 1), ("delete", 2), ("modify", 3))

class MasterValidValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class DTIPortID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dtiin1", 1), ("dtiin2", 2), ("dtiout1", 3), ("dtiout2", 4))

class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

dtiStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 1))
dtiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 2))
dtiConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3))
if mibBuilder.loadTexts: dtiConformance.setStatus('current')
if mibBuilder.loadTexts: dtiConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
dtiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3, 1))
dtiUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3, 2))
mibBuilder.exportSymbols("SYMMCOMMONDTI", TSsm=TSsm, DTIPortID=DTIPortID, PYSNMP_MODULE_ID=symmDti, dtiConfig=dtiConfig, YesValue=YesValue, DateAndTime=DateAndTime, TableRowChange=TableRowChange, OpMode=OpMode, TLocalTimeOffset=TLocalTimeOffset, OnValue=OnValue, OkValue=OkValue, ActionApply=ActionApply, dtiCompliances=dtiCompliances, TAntHeight=TAntHeight, TLatAndLon=TLatAndLon, EnaValue=EnaValue, symmDti=symmDti, TPModuleID=TPModuleID, dtiConformance=dtiConformance, MasterValidValue=MasterValidValue, ActiveValue=ActiveValue, dtiUocGroups=dtiUocGroups, ValidValue=ValidValue, dtiStatus=dtiStatus)

#
# PySNMP MIB module FSS-SYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-SYSTEM
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
fssCommon, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Gauge32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, Counter32, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Gauge32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "Counter32", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
fssSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100))
fssSystem.setRevisions(('2016-06-20 00:00',))
if mibBuilder.loadTexts: fssSystem.setLastUpdated('201606200000Z')
if mibBuilder.loadTexts: fssSystem.setOrganization('Fujitsu Network Communications, Inc.')
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ADT_value(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("adt-zero", 0), ("adt-ten", 1))

class RestartLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cold", 0), ("warm", 1))

class AAT_value(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aat-zero", 0), ("aat-twoPointFive", 1))

system = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1))
systemVendor = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 1), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemVendor.setStatus('current')
systemName = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(7, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemName.setStatus('current')
systemLocation = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 3), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemLocation.setStatus('current')
systemContact = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 4), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemContact.setStatus('current')
systemNeType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemNeType.setStatus('current')
systemSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 6), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSoftwareVersion.setStatus('current')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
systemAutoP = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAutoP.setStatus('current')
systemAAT = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 9), AAT_value()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAAT.setStatus('current')
systemADT = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 10), ADT_value()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemADT.setStatus('current')
systemClock = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11))
systemClockTimezone_name = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11, 1), String()).setLabel("systemClockTimezone-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemClockTimezone_name.setStatus('current')
systemNtp = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp.setStatus('current')
systemNtpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtpEnabled.setStatus('current')
systemNtp_cfg = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 14), TruthValue()).setLabel("systemNtp-cfg").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp_cfg.setStatus('current')
systemNtp_cfgNtp_enabled = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 15), TruthValue()).setLabel("systemNtp-cfgNtp-enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp_cfgNtp_enabled.setStatus('current')
system_state = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2)).setLabel("system-state")
system_stateClock = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1)).setLabel("system-stateClock")
system_stateClockDatetime = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1, 1), String()).setLabel("system-stateClockDatetime").setMaxAccess("readonly")
if mibBuilder.loadTexts: system_stateClockDatetime.setStatus('current')
mibBuilder.exportSymbols("FSS-SYSTEM", system_state=system_state, system_stateClock=system_stateClock, system_stateClockDatetime=system_stateClockDatetime, systemADT=systemADT, systemAAT=systemAAT, system=system, systemClockTimezone_name=systemClockTimezone_name, systemNtpEnabled=systemNtpEnabled, systemNeType=systemNeType, systemNtp_cfgNtp_enabled=systemNtp_cfgNtp_enabled, systemContact=systemContact, AAT_value=AAT_value, systemVendor=systemVendor, systemLocation=systemLocation, systemName=systemName, systemClock=systemClock, fssSystem=fssSystem, systemNtp=systemNtp, ADT_value=ADT_value, systemUpTime=systemUpTime, String=String, RestartLevel=RestartLevel, systemAutoP=systemAutoP, systemNtp_cfg=systemNtp_cfg, PYSNMP_MODULE_ID=fssSystem, systemSoftwareVersion=systemSoftwareVersion)

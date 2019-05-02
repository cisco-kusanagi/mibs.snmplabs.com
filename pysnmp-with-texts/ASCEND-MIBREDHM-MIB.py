#
# PySNMP MIB module ASCEND-MIBREDHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBREDHM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, MibIdentifier, NotificationType, Counter64, iso, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Counter64", "iso", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibredHealthMonitoringProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 179))
mibredHealthMonitoringProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 179, 1), )
if mibBuilder.loadTexts: mibredHealthMonitoringProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibredHealthMonitoringProfileTable.setDescription('A list of mibredHealthMonitoringProfile profile entries.')
mibredHealthMonitoringProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1), ).setIndexNames((0, "ASCEND-MIBREDHM-MIB", "redHealthMonitoringProfile-Index-o"))
if mibBuilder.loadTexts: mibredHealthMonitoringProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibredHealthMonitoringProfileEntry.setDescription('A mibredHealthMonitoringProfile entry containing objects that maps to the parameters of mibredHealthMonitoringProfile profile.')
redHealthMonitoringProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 1), Integer32()).setLabel("redHealthMonitoringProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redHealthMonitoringProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_Index_o.setDescription('')
redHealthMonitoringProfile_HmEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("redHealthMonitoringProfile-HmEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_HmEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_HmEnabled.setDescription('Indicates whether health monitoring feature is enabled. Redundancy feature has to be enabled prior to this feature')
redHealthMonitoringProfile_MaxWarningPrimary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 3), Integer32()).setLabel("redHealthMonitoringProfile-MaxWarningPrimary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPrimary.setDescription('Maximum of total warnings allowed for primary, When the total warnings exceeds this maximum, controller will reset.')
redHealthMonitoringProfile_MaxWarningSecondary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 4), Integer32()).setLabel("redHealthMonitoringProfile-MaxWarningSecondary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningSecondary.setDescription('Maximum of total warnings allowed for secondary, When the total warnings exceeds this maximum, controller will reset. Secondary should have a more stringent value than primary.')
redHealthMonitoringProfile_MaxWarningPerMinutePrimary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 5), Integer32()).setLabel("redHealthMonitoringProfile-MaxWarningPerMinutePrimary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPerMinutePrimary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPerMinutePrimary.setDescription('Maximum of total warning per minute allowed for primary.')
redHealthMonitoringProfile_MaxWarningPerMinuteSecondary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 6), Integer32()).setLabel("redHealthMonitoringProfile-MaxWarningPerMinuteSecondary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPerMinuteSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MaxWarningPerMinuteSecondary.setDescription('Maximum of total warning per minute allowed for secondary. Secondary should have a more stringent value than primary.')
redHealthMonitoringProfile_MemoryThresholdPrimary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 7), Integer32()).setLabel("redHealthMonitoringProfile-MemoryThresholdPrimary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryThresholdPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryThresholdPrimary.setDescription('Percent threshold for available memory on primary, controller resets when memory is lower than the threshold.')
redHealthMonitoringProfile_MemoryThresholdSecondary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 8), Integer32()).setLabel("redHealthMonitoringProfile-MemoryThresholdSecondary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryThresholdSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryThresholdSecondary.setDescription('Percent threshold for available memory on secondary, controller resets when memory is lower than the threshold. Secondary should have a more stringent value than primary.')
redHealthMonitoringProfile_MemoryAlertThresholdPrimary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 9), Integer32()).setLabel("redHealthMonitoringProfile-MemoryAlertThresholdPrimary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertThresholdPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertThresholdPrimary.setDescription('Percent threshold for memory alert polling on primary, when memory level is lower than the threshold, log message will be sent out.')
redHealthMonitoringProfile_MemoryAlertThresholdSecondary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 10), Integer32()).setLabel("redHealthMonitoringProfile-MemoryAlertThresholdSecondary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertThresholdSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertThresholdSecondary.setDescription('Percent threshold for memory alert polling on secondary, when memory level is lower than the threshold, log message will be sent out.')
redHealthMonitoringProfile_MemoryAlertTimeoutPrimary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 11), Integer32()).setLabel("redHealthMonitoringProfile-MemoryAlertTimeoutPrimary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertTimeoutPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertTimeoutPrimary.setDescription('Maximum time (in sec) allowed for memory level stays continuously below memory-alert-threshold-primary.')
redHealthMonitoringProfile_MemoryAlertTimeoutSecondary = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 12), Integer32()).setLabel("redHealthMonitoringProfile-MemoryAlertTimeoutSecondary").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertTimeoutSecondary.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_MemoryAlertTimeoutSecondary.setDescription('Maximum time (in sec) allowed for memory level stays continuously below memory-alert-threshold-secondary.')
redHealthMonitoringProfile_ResetStuckPrimaryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 13), Integer32()).setLabel("redHealthMonitoringProfile-ResetStuckPrimaryTimeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_ResetStuckPrimaryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_ResetStuckPrimaryTimeout.setDescription('secondary resets primary if no response from primary exceeds this timeout (in seconds). Minimum is 3 seconds.')
redHealthMonitoringProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("redHealthMonitoringProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redHealthMonitoringProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: redHealthMonitoringProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBREDHM-MIB", redHealthMonitoringProfile_MemoryAlertTimeoutSecondary=redHealthMonitoringProfile_MemoryAlertTimeoutSecondary, redHealthMonitoringProfile_Action_o=redHealthMonitoringProfile_Action_o, redHealthMonitoringProfile_MaxWarningPerMinuteSecondary=redHealthMonitoringProfile_MaxWarningPerMinuteSecondary, redHealthMonitoringProfile_Index_o=redHealthMonitoringProfile_Index_o, redHealthMonitoringProfile_MemoryThresholdPrimary=redHealthMonitoringProfile_MemoryThresholdPrimary, redHealthMonitoringProfile_MemoryAlertThresholdSecondary=redHealthMonitoringProfile_MemoryAlertThresholdSecondary, redHealthMonitoringProfile_ResetStuckPrimaryTimeout=redHealthMonitoringProfile_ResetStuckPrimaryTimeout, DisplayString=DisplayString, mibredHealthMonitoringProfile=mibredHealthMonitoringProfile, mibredHealthMonitoringProfileEntry=mibredHealthMonitoringProfileEntry, redHealthMonitoringProfile_MemoryAlertTimeoutPrimary=redHealthMonitoringProfile_MemoryAlertTimeoutPrimary, redHealthMonitoringProfile_MemoryAlertThresholdPrimary=redHealthMonitoringProfile_MemoryAlertThresholdPrimary, redHealthMonitoringProfile_MaxWarningSecondary=redHealthMonitoringProfile_MaxWarningSecondary, mibredHealthMonitoringProfileTable=mibredHealthMonitoringProfileTable, redHealthMonitoringProfile_MaxWarningPrimary=redHealthMonitoringProfile_MaxWarningPrimary, redHealthMonitoringProfile_HmEnabled=redHealthMonitoringProfile_HmEnabled, redHealthMonitoringProfile_MemoryThresholdSecondary=redHealthMonitoringProfile_MemoryThresholdSecondary, redHealthMonitoringProfile_MaxWarningPerMinutePrimary=redHealthMonitoringProfile_MaxWarningPerMinutePrimary)

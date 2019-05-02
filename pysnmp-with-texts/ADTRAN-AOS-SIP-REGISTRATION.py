#
# PySNMP MIB module ADTRAN-AOS-SIP-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-0.3.4 at Wed May  1 11:14:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, Gauge32, Unsigned32, Bits, NotificationType, MibIdentifier, iso, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "NotificationType", "MibIdentifier", "iso", "IpAddress", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipRegistration = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4))
adGenAOSSipRegistration.setRevisions(('2010-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSSipRegistration.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSSipRegistration.setLastUpdated('201011020000Z')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setContactInfo('Technical Support Dept. Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 800 726-8663 Fax: +1 256 963 6217 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setDescription('This MIB contains information regarding SIP registrations.')
adSipRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4))
adSipRegistrationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0))
adSipTrunkRegistrationAlarmTrunkIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setDescription('This DisplayString contains the three digit (i.e. T01) trunk identifier associated with this failed REGISTER attempt.')
adSipTrunkRegistrationAlarmSipIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setDescription('This DisplayString represents the SIP identity for a failed REGISTER attempt.')
adSipTrunkRegistrationAlarmRegistrar = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setDescription('The adSipTrunkRegistrationAlarmRegistrar contains the IP address of the SIP registrar for a failed REGISTER attempt.')
adSipTrunkRegistrationAlarmTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setDescription('The time (seconds since epoch) that a failed REGISTER attempt occurred and not necessarily the when the trap was sent.')
adSipTrunkRegistrationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setDescription('This trap indicates that a SIP trunk registration attempt failed. The sysName is the exact same as defined in SNMPv2-MIB. adSipTrunkRegistrationAlarmTrunkIdentity specifies the three character trunk identity associated with the failed attempt. The corresponding SIP identity and registrar server are contained in adSipTrunkRegistrationAlarmSipIdentity and adSipTrunkRegistrationAlarmRegistrar respectively. The adSipTrunkRegistrationAlarmTimestamp indicates when this condition occurred and not necessarily when the trap was sent. ')
adSipRegistrationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12))
adSipRegistrationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1))
adSipRegistrationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2))
adSipRegistrationFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationFullCompliance = adSipRegistrationFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationFullCompliance.setDescription('The compliance statement for SNMP entities which implement version 2 of the adGenAosSipRegistration MIB. When this MIB is fully implemented, then such an implementation can claim full compliance.')
adSipRegistrationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationGroup = adSipRegistrationNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationNotificationGroup.setDescription('This group contains notifications about SIP registration conditions.')
adSipRegistrationNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationUtilityGroup = adSipRegistrationNotificationUtilityGroup.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationNotificationUtilityGroup.setDescription('A collection of objects accessible only for notifications.')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-REGISTRATION", adSipRegistrationCompliances=adSipRegistrationCompliances, adSipTrunkRegistrationAlarmSipIdentity=adSipTrunkRegistrationAlarmSipIdentity, adSipRegistrationFullCompliance=adSipRegistrationFullCompliance, adSipRegistrationConformance=adSipRegistrationConformance, PYSNMP_MODULE_ID=adGenAOSSipRegistration, adSipRegistrationGroups=adSipRegistrationGroups, adSipTrunkRegistrationAlarmTimestamp=adSipTrunkRegistrationAlarmTimestamp, adSipRegistrationNotificationGroup=adSipRegistrationNotificationGroup, adSipTrunkRegistrationAlarm=adSipTrunkRegistrationAlarm, adSipRegistrationNotificationUtilityGroup=adSipRegistrationNotificationUtilityGroup, adSipRegistrationTraps=adSipRegistrationTraps, adSipTrunkRegistrationAlarmTrunkIdentity=adSipTrunkRegistrationAlarmTrunkIdentity, adSipTrunkRegistrationAlarmRegistrar=adSipTrunkRegistrationAlarmRegistrar, adGenAOSSipRegistration=adGenAOSSipRegistration, adSipRegistration=adSipRegistration)

#
# PySNMP MIB module ADTRAN-AOS-SIP-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-0.3.4 at Mon Apr 29 16:58:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
NotificationType, ModuleIdentity, Bits, iso, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, TimeTicks, Counter32, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Bits", "iso", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "TimeTicks", "Counter32", "IpAddress", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipRegistration = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4))
adGenAOSSipRegistration.setRevisions(('2010-11-02 00:00',))
if mibBuilder.loadTexts: adGenAOSSipRegistration.setLastUpdated('201011020000Z')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setOrganization('ADTRAN, Inc.')
adSipRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4))
adSipRegistrationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0))
adSipTrunkRegistrationAlarmTrunkIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setStatus('current')
adSipTrunkRegistrationAlarmSipIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setStatus('current')
adSipTrunkRegistrationAlarmRegistrar = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setStatus('current')
adSipTrunkRegistrationAlarmTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setStatus('current')
adSipTrunkRegistrationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setStatus('current')
adSipRegistrationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12))
adSipRegistrationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1))
adSipRegistrationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2))
adSipRegistrationFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationFullCompliance = adSipRegistrationFullCompliance.setStatus('current')
adSipRegistrationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationGroup = adSipRegistrationNotificationGroup.setStatus('current')
adSipRegistrationNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationUtilityGroup = adSipRegistrationNotificationUtilityGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-REGISTRATION", adSipRegistrationTraps=adSipRegistrationTraps, adSipTrunkRegistrationAlarmSipIdentity=adSipTrunkRegistrationAlarmSipIdentity, adSipRegistrationConformance=adSipRegistrationConformance, adSipRegistrationFullCompliance=adSipRegistrationFullCompliance, adSipTrunkRegistrationAlarmRegistrar=adSipTrunkRegistrationAlarmRegistrar, PYSNMP_MODULE_ID=adGenAOSSipRegistration, adSipRegistrationNotificationUtilityGroup=adSipRegistrationNotificationUtilityGroup, adSipTrunkRegistrationAlarm=adSipTrunkRegistrationAlarm, adSipTrunkRegistrationAlarmTrunkIdentity=adSipTrunkRegistrationAlarmTrunkIdentity, adSipRegistrationGroups=adSipRegistrationGroups, adSipTrunkRegistrationAlarmTimestamp=adSipTrunkRegistrationAlarmTimestamp, adGenAOSSipRegistration=adGenAOSSipRegistration, adSipRegistrationNotificationGroup=adSipRegistrationNotificationGroup, adSipRegistrationCompliances=adSipRegistrationCompliances, adSipRegistration=adSipRegistration)

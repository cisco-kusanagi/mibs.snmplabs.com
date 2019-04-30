#
# PySNMP MIB module SPIDCOM-TRAPS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-TRAPS
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
plcBasePortIndex, = mibBuilder.importSymbols("SPC200", "plcBasePortIndex")
ItuAlarmProbableCause, ItuAlarmType, neAlarmActivePhoto = mibBuilder.importSymbols("SPIDCOM-ALARM-MIB", "ItuAlarmProbableCause", "ItuAlarmType", "neAlarmActivePhoto")
specificSpidcomTrap, = mibBuilder.importSymbols("SPIDCOM-NOTIFICATION-MIB", "specificSpidcomTrap")
trapsDefinition = ModuleIdentity((1, 3, 6, 1, 4, 1, 22764, 4, 1))
if mibBuilder.loadTexts: trapsDefinition.setLastUpdated('200207151330Z')
if mibBuilder.loadTexts: trapsDefinition.setOrganization('SPiDCOM')
deviceDown = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 1))
if mibBuilder.loadTexts: deviceDown.setStatus('current')
deviceUp = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 2))
if mibBuilder.loadTexts: deviceUp.setStatus('current')
maxAttenuation = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 3))
if mibBuilder.loadTexts: maxAttenuation.setStatus('current')
maxNoise = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 4))
if mibBuilder.loadTexts: maxNoise.setStatus('current')
linkUpDownNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 11)).setObjects(("SPIDCOM-TRAPS", "deviceUp"), ("SPIDCOM-TRAPS", "deviceDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linkUpDownNotificationsGroup = linkUpDownNotificationsGroup.setStatus('current')
maxAttenuationNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 12)).setObjects(("SPIDCOM-TRAPS", "maxAttenuation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxAttenuationNotificationsGroup = maxAttenuationNotificationsGroup.setStatus('current')
maxNoiseNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 13)).setObjects(("SPIDCOM-TRAPS", "maxNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxNoiseNotificationsGroup = maxNoiseNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("SPIDCOM-TRAPS", PYSNMP_MODULE_ID=trapsDefinition, linkUpDownNotificationsGroup=linkUpDownNotificationsGroup, deviceDown=deviceDown, maxNoise=maxNoise, maxNoiseNotificationsGroup=maxNoiseNotificationsGroup, maxAttenuationNotificationsGroup=maxAttenuationNotificationsGroup, deviceUp=deviceUp, trapsDefinition=trapsDefinition, maxAttenuation=maxAttenuation)

#
# PySNMP MIB module HP-ICF-USBPORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-USBPORT
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, MibIdentifier, Gauge32, TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfUSBPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53))
hpicfUSBPortMIB.setRevisions(('2009-03-11 00:00', '2008-09-17 00:00', '2008-09-10 00:00', '2008-06-25 00:00',))
if mibBuilder.loadTexts: hpicfUSBPortMIB.setLastUpdated('200903110000Z')
if mibBuilder.loadTexts: hpicfUSBPortMIB.setOrganization('HP Networking')
hpicfUSBPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1))
hpicfUSBPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notPresent", 0), ("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUSBPortStatus.setStatus('current')
hpicfUSBPortZeroPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("powerUnavailable", 0), ("powerOff", 1), ("powerOn", 2))).clone('powerOn')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUSBPortZeroPowerStatus.setStatus('current')
hpicfUSBPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0))
hpicfUSBPortEnabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 1))
if mibBuilder.loadTexts: hpicfUSBPortEnabled.setStatus('current')
hpicfUSBPortDisabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 2))
if mibBuilder.loadTexts: hpicfUSBPortDisabled.setStatus('current')
hpicfUSBPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2))
hpicfUSBPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1))
hpicfUSBPortBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 1)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortStatus"), ("HP-ICF-USBPORT", "hpicfUSBPortZeroPowerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortBaseGroup = hpicfUSBPortBaseGroup.setStatus('current')
hpicfUSBPortNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 2)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortEnabled"), ("HP-ICF-USBPORT", "hpicfUSBPortDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortNotificationGroup = hpicfUSBPortNotificationGroup.setStatus('current')
hpicfUSBPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2))
hpicfUSBPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2, 1)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortBaseGroup"), ("HP-ICF-USBPORT", "hpicfUSBPortNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortCompliance = hpicfUSBPortCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-USBPORT", hpicfUSBPortNotifications=hpicfUSBPortNotifications, hpicfUSBPortConfig=hpicfUSBPortConfig, hpicfUSBPortStatus=hpicfUSBPortStatus, hpicfUSBPortNotificationGroup=hpicfUSBPortNotificationGroup, hpicfUSBPortCompliances=hpicfUSBPortCompliances, hpicfUSBPortMIB=hpicfUSBPortMIB, PYSNMP_MODULE_ID=hpicfUSBPortMIB, hpicfUSBPortCompliance=hpicfUSBPortCompliance, hpicfUSBPortConformance=hpicfUSBPortConformance, hpicfUSBPortZeroPowerStatus=hpicfUSBPortZeroPowerStatus, hpicfUSBPortDisabled=hpicfUSBPortDisabled, hpicfUSBPortBaseGroup=hpicfUSBPortBaseGroup, hpicfUSBPortEnabled=hpicfUSBPortEnabled, hpicfUSBPortGroups=hpicfUSBPortGroups)

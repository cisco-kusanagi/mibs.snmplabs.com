#
# PySNMP MIB module HP-ICF-USBPORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-USBPORT
# Produced by pysmi-0.3.4 at Wed May  1 13:35:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Unsigned32, Gauge32, IpAddress, NotificationType, iso, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "NotificationType", "iso", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfUSBPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53))
hpicfUSBPortMIB.setRevisions(('2009-03-11 00:00', '2008-09-17 00:00', '2008-09-10 00:00', '2008-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfUSBPortMIB.setRevisionsDescriptions(('Add hpicfUSBPortZeroPowerStatus object ', 'Move NOTIFICATIONS OID from 3 to 0', 'Added NOTIFICATIONS for enabled/disabled', 'Original version',))
if mibBuilder.loadTexts: hpicfUSBPortMIB.setLastUpdated('200903110000Z')
if mibBuilder.loadTexts: hpicfUSBPortMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfUSBPortMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfUSBPortMIB.setDescription('This MIB module manages the USB Port.')
hpicfUSBPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1))
hpicfUSBPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notPresent", 0), ("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUSBPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortStatus.setDescription('hpicfUSBPortStatus control whether or not the USB port is enabled. notPresent(0) - USBPort is not present enabled(1) - USBPort Enabled. disabled(2) - USBPort Disabled. ')
hpicfUSBPortZeroPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("powerUnavailable", 0), ("powerOff", 1), ("powerOn", 2))).clone('powerOn')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUSBPortZeroPowerStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortZeroPowerStatus.setDescription('hpicfUSBPortZeroPowerStatus indicates if the USB port zero power is on or off. powerUnavailable(0) - USBPort power reading is unavailable. powerOff(1) - USBPort power is off. powerOn(2) - USBPort power is on. ')
hpicfUSBPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0))
hpicfUSBPortEnabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 1))
if mibBuilder.loadTexts: hpicfUSBPortEnabled.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortEnabled.setDescription("An hpicfUSBPortEnabled notification signifies that the SNMP entity, acting in an agent role, has detected that the hpicfUSBPortStatus object has transitioned into the 'enabled' state.")
hpicfUSBPortDisabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 2))
if mibBuilder.loadTexts: hpicfUSBPortDisabled.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortDisabled.setDescription("An hpicfUSBPortDisabled notification signifies that the SNMP entity, acting in an agent role, has detected that the hpicfUSBPortStatus object has transitioned into the 'disabled' state.")
hpicfUSBPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2))
hpicfUSBPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1))
hpicfUSBPortBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 1)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortStatus"), ("HP-ICF-USBPORT", "hpicfUSBPortZeroPowerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortBaseGroup = hpicfUSBPortBaseGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortBaseGroup.setDescription('A mandatory group with an object to enable or disable the USB port.')
hpicfUSBPortNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 2)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortEnabled"), ("HP-ICF-USBPORT", "hpicfUSBPortDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortNotificationGroup = hpicfUSBPortNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortNotificationGroup.setDescription('The hpicfUSBPort MIB Notification Group.')
hpicfUSBPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2))
hpicfUSBPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2, 1)).setObjects(("HP-ICF-USBPORT", "hpicfUSBPortBaseGroup"), ("HP-ICF-USBPORT", "hpicfUSBPortNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUSBPortCompliance = hpicfUSBPortCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfUSBPortCompliance.setDescription('Compliance statement for HP ICF USBPort configuration')
mibBuilder.exportSymbols("HP-ICF-USBPORT", hpicfUSBPortConformance=hpicfUSBPortConformance, hpicfUSBPortConfig=hpicfUSBPortConfig, hpicfUSBPortCompliance=hpicfUSBPortCompliance, hpicfUSBPortBaseGroup=hpicfUSBPortBaseGroup, hpicfUSBPortMIB=hpicfUSBPortMIB, hpicfUSBPortNotifications=hpicfUSBPortNotifications, hpicfUSBPortStatus=hpicfUSBPortStatus, hpicfUSBPortDisabled=hpicfUSBPortDisabled, hpicfUSBPortGroups=hpicfUSBPortGroups, hpicfUSBPortNotificationGroup=hpicfUSBPortNotificationGroup, PYSNMP_MODULE_ID=hpicfUSBPortMIB, hpicfUSBPortEnabled=hpicfUSBPortEnabled, hpicfUSBPortCompliances=hpicfUSBPortCompliances, hpicfUSBPortZeroPowerStatus=hpicfUSBPortZeroPowerStatus)

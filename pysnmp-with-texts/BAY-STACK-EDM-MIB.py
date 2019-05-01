#
# PySNMP MIB module BAY-STACK-EDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-EDM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Integer32, TimeTicks, IpAddress, Counter64, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Integer32", "TimeTicks", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEdmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 36))
bayStackEdmMib.setRevisions(('2013-10-11 00:00', '2013-02-13 00:00', '2009-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackEdmMib.setRevisionsDescriptions(('v3: Added Integer32 to IMPORTS.', 'v2: Added bsEdmInactivityTimeout object.', 'v1: Initial version.',))
if mibBuilder.loadTexts: bayStackEdmMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackEdmMib.setOrganization('Avaya Networks')
if mibBuilder.loadTexts: bayStackEdmMib.setContactInfo('Avaya Networks')
if mibBuilder.loadTexts: bayStackEdmMib.setDescription("Enterprise Device Manager (EDM) MIB for the Avaya stackable Ethernet Routing Switches family Copyright 2013 Avaya Networks All rights reserved. This Avaya Networks SNMP Management Information Base Specification embodies Avaya Networks' confidential and proprietary intellectual property. Avaya Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bayStackEdmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 0))
bayStackEdmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1))
bsEdmScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1))
bsEdmHelpFilePath = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 327))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmHelpFilePath.setStatus('current')
if mibBuilder.loadTexts: bsEdmHelpFilePath.setDescription("This object is used to specify the location of the EDM help file. The value is an ASCII string similar to a URL, and must be in one of the following formats: - 'usb://<filename>' - the help file is located on the usb port of the switch, if not in stack, or on the usb port of the base unit, if in stack. - 'usb://<unit-number>/<filename>' - the help file is located on the usb port of the switch, if not in stack, or on the usb port of the specified unit, if in stack. The unit number must be between 1 and 8. - 'tftp://<ip-address>/<filename>' - the help file is located on the TFTP server at the specified IP address. - 'tftp://<hostname>/<filename>' - the help file is located on the TFTP server at the specified host. The hostname must have at most 64 characters in length. In each of the supported formats, the filename must have at most 255 characters in length.")
bsEdmInactivityTimeout = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmInactivityTimeout.setStatus('current')
if mibBuilder.loadTexts: bsEdmInactivityTimeout.setDescription('Used to indicate the amount of idle time, in seconds, to wait before timing out an EDM session.')
mibBuilder.exportSymbols("BAY-STACK-EDM-MIB", PYSNMP_MODULE_ID=bayStackEdmMib, bsEdmHelpFilePath=bsEdmHelpFilePath, bayStackEdmMib=bayStackEdmMib, bsEdmScalars=bsEdmScalars, bayStackEdmNotifications=bayStackEdmNotifications, bayStackEdmObjects=bayStackEdmObjects, bsEdmInactivityTimeout=bsEdmInactivityTimeout)

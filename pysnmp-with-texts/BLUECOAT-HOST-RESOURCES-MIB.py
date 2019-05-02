#
# PySNMP MIB module BLUECOAT-HOST-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-HOST-RESOURCES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter64, TimeTicks, IpAddress, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, ModuleIdentity, Integer32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "TimeTicks", "IpAddress", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "ModuleIdentity", "Integer32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
blueCoatHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 9))
blueCoatHostResourcesMIB.setRevisions(('2007-04-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setRevisionsDescriptions(('Marked as deprecated.',))
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setLastUpdated('200704240000Z')
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setOrganization('Blue Coat')
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setDescription('Internal MIB defines Blue Coat device serial number for Blue Coat Director use.')
bchrDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1))
bchrSerial = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bchrSerial.setStatus('deprecated')
if mibBuilder.loadTexts: bchrSerial.setDescription('Serial number of the Blue Coat device.')
mibBuilder.exportSymbols("BLUECOAT-HOST-RESOURCES-MIB", bchrDevice=bchrDevice, blueCoatHostResourcesMIB=blueCoatHostResourcesMIB, bchrSerial=bchrSerial, PYSNMP_MODULE_ID=blueCoatHostResourcesMIB)

#
# PySNMP MIB module BLUECOAT-HOST-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-HOST-RESOURCES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, IpAddress, Unsigned32, TimeTicks, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
blueCoatHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 9))
blueCoatHostResourcesMIB.setRevisions(('2007-04-24 00:00',))
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setLastUpdated('200704240000Z')
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setOrganization('Blue Coat')
bchrDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1))
bchrSerial = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bchrSerial.setStatus('deprecated')
mibBuilder.exportSymbols("BLUECOAT-HOST-RESOURCES-MIB", bchrDevice=bchrDevice, PYSNMP_MODULE_ID=blueCoatHostResourcesMIB, bchrSerial=bchrSerial, blueCoatHostResourcesMIB=blueCoatHostResourcesMIB)

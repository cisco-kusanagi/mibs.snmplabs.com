#
# PySNMP MIB module TOASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOASTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, NotificationType, MibIdentifier, Gauge32, ObjectIdentity, Bits, Integer32, Counter32, IpAddress, enterprises, ModuleIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "NotificationType", "MibIdentifier", "Gauge32", "ObjectIdentity", "Bits", "Integer32", "Counter32", "IpAddress", "enterprises", "ModuleIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
epilogue = MibIdentifier((1, 3, 6, 1, 4, 1, 12))
toaster = MibIdentifier((1, 3, 6, 1, 4, 1, 12, 2))
toasterManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: toasterManufacturer.setStatus('mandatory')
toasterModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: toasterModelNumber.setStatus('mandatory')
toasterControl = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterControl.setStatus('mandatory')
toasterDoneness = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterDoneness.setStatus('mandatory')
toasterToastType = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("white-bread", 1), ("wheat-bread", 2), ("wonder-bread", 3), ("frozen-waffle", 4), ("frozen-bagel", 5), ("hash-brown", 6), ("other", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterToastType.setStatus('mandatory')
mibBuilder.exportSymbols("TOASTER-MIB", toasterDoneness=toasterDoneness, epilogue=epilogue, toasterControl=toasterControl, toasterManufacturer=toasterManufacturer, toasterModelNumber=toasterModelNumber, toasterToastType=toasterToastType, toaster=toaster)

#
# PySNMP MIB module XYLAN-FW1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-FW1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, enterprises, IpAddress, MibIdentifier, Integer32, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Bits, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "enterprises", "IpAddress", "MibIdentifier", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "iso", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

checkpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 1919))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1))
fw = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1, 1))
fwModuleState = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleState.setStatus('mandatory')
fwFilterName = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterName.setStatus('mandatory')
fwFilterDate = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterDate.setStatus('mandatory')
fwAccepted = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwAccepted.setStatus('mandatory')
fwRejected = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwRejected.setStatus('mandatory')
fwDropped = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDropped.setStatus('mandatory')
fwLogged = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwLogged.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-FW1-MIB", checkpoint=checkpoint, fwFilterDate=fwFilterDate, fw=fw, fwLogged=fwLogged, products=products, fwRejected=fwRejected, fwModuleState=fwModuleState, DisplayString=DisplayString, fwFilterName=fwFilterName, fwAccepted=fwAccepted, fwDropped=fwDropped)

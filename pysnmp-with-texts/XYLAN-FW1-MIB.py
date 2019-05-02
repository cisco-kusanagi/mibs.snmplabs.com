#
# PySNMP MIB module XYLAN-FW1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-FW1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:45:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, enterprises, TimeTicks, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "enterprises", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

checkpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 1919))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1))
fw = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1, 1))
fwModuleState = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleState.setStatus('mandatory')
if mibBuilder.loadTexts: fwModuleState.setDescription('The state of the fw module.')
fwFilterName = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: fwFilterName.setDescription('The name of the loaded filter.')
fwFilterDate = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterDate.setStatus('mandatory')
if mibBuilder.loadTexts: fwFilterDate.setDescription('When installated (STRING!)')
fwAccepted = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwAccepted.setStatus('mandatory')
if mibBuilder.loadTexts: fwAccepted.setDescription('The number accepted packets.')
fwRejected = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwRejected.setStatus('mandatory')
if mibBuilder.loadTexts: fwRejected.setDescription('The number accepted packets.')
fwDropped = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDropped.setStatus('mandatory')
if mibBuilder.loadTexts: fwDropped.setDescription('The number accepted packets.')
fwLogged = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwLogged.setStatus('mandatory')
if mibBuilder.loadTexts: fwLogged.setDescription('The number accepted packets.')
mibBuilder.exportSymbols("XYLAN-FW1-MIB", DisplayString=DisplayString, fwLogged=fwLogged, fwDropped=fwDropped, fwModuleState=fwModuleState, fw=fw, fwFilterDate=fwFilterDate, fwAccepted=fwAccepted, products=products, fwRejected=fwRejected, fwFilterName=fwFilterName, checkpoint=checkpoint)

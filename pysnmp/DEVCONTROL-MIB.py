#
# PySNMP MIB module DEVCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVCONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, MibIdentifier, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Counter32, Gauge32, ObjectIdentity, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
aniDevControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 4))
if mibBuilder.loadTexts: aniDevControl.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevControl.setOrganization('Aperto Networks')
aniDevControlResetDevice = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlResetDevice.setStatus('current')
aniDevControlSetFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlSetFactoryDefaults.setStatus('current')
aniDevControlStartUpload = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlStartUpload.setStatus('current')
aniDevControlUploadState = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("successful", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlUploadState.setStatus('current')
mibBuilder.exportSymbols("DEVCONTROL-MIB", aniDevControlStartUpload=aniDevControlStartUpload, aniDevControlSetFactoryDefaults=aniDevControlSetFactoryDefaults, PYSNMP_MODULE_ID=aniDevControl, aniDevControlUploadState=aniDevControlUploadState, aniDevControlResetDevice=aniDevControlResetDevice, aniDevControl=aniDevControl)

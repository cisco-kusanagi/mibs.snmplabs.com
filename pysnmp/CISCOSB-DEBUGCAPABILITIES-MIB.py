#
# PySNMP MIB module CISCOSB-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-DEBUGCAPABILITIES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, ObjectIdentity, ModuleIdentity, IpAddress, Counter32, Unsigned32, Gauge32, Counter64, MibIdentifier, Integer32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "Counter64", "MibIdentifier", "Integer32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('Cisco Small Business')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-DEBUGCAPABILITIES-MIB", PYSNMP_MODULE_ID=rlDebugCapabilities, rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities)

#
# PySNMP MIB module Wellfleet-FAKE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-FAKE-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, ModuleIdentity, Counter64, NotificationType, Bits, mgmt, TimeTicks, Opaque, NotificationType, MibIdentifier, Integer32, IpAddress, enterprises, mib_2, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ModuleIdentity", "Counter64", "NotificationType", "Bits", "mgmt", "TimeTicks", "Opaque", "NotificationType", "MibIdentifier", "Integer32", "IpAddress", "enterprises", "mib-2", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfSnmpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSnmpGroup")
wfFakeEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4))
wfFakeEventString = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFakeEventString.setStatus('mandatory')
wfLogTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fault", 1), ("warning", 2), ("informational", 3), ("trace", 4), ("debug", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLogTrapSeverity.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-FAKE-EVENT-MIB", wfLogTrapSeverity=wfLogTrapSeverity, wfFakeEvent=wfFakeEvent, wfFakeEventString=wfFakeEventString)

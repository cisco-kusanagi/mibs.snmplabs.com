#
# PySNMP MIB module Wellfleet-FAKE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-FAKE-EVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Unsigned32, MibIdentifier, iso, Gauge32, Opaque, NotificationType, Bits, Counter32, mib_2, mgmt, TimeTicks, IpAddress, ModuleIdentity, enterprises, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "iso", "Gauge32", "Opaque", "NotificationType", "Bits", "Counter32", "mib-2", "mgmt", "TimeTicks", "IpAddress", "ModuleIdentity", "enterprises", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfSnmpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSnmpGroup")
wfFakeEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4))
wfFakeEventString = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFakeEventString.setStatus('mandatory')
if mibBuilder.loadTexts: wfFakeEventString.setDescription('A dummy display string. While no string will actually be kept here, the full identifier (object id + attribute id + instance ID ) will be used to wrap event strings passed from the system logger into an SNMP Trap message.')
wfLogTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fault", 1), ("warning", 2), ("informational", 3), ("trace", 4), ("debug", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLogTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: wfLogTrapSeverity.setDescription('This object is used for wrapping log event severity information in a log event specific trap. The severity information is the thrid variable binding in a log event specific trap.')
mibBuilder.exportSymbols("Wellfleet-FAKE-EVENT-MIB", wfFakeEventString=wfFakeEventString, wfLogTrapSeverity=wfLogTrapSeverity, wfFakeEvent=wfFakeEvent)

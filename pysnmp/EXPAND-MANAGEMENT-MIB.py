#
# PySNMP MIB module EXPAND-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
management, = mibBuilder.importSymbols("EXPAND-NETWORKS-SMI", "management")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Counter64, MibIdentifier, IpAddress, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter64", "MibIdentifier", "IpAddress", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
log = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1))
events = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1))
general = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1))
severity = MibScalar((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("deb", 1), ("info", 2), ("audit", 3), ("warning", 4), ("error", 5), ("fatal", 6), ("max-severity", 7), ("beta", 8), ("overide", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('mandatory')
message = MibScalar((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: message.setStatus('mandatory')
mibBuilder.exportSymbols("EXPAND-MANAGEMENT-MIB", message=message, log=log, events=events, general=general, severity=severity)

#
# PySNMP MIB module EXPAND-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
management, = mibBuilder.importSymbols("EXPAND-NETWORKS-SMI", "management")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Gauge32, TimeTicks, Integer32, Unsigned32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Unsigned32", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
log = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1))
events = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1))
general = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1))
severity = MibScalar((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("deb", 1), ("info", 2), ("audit", 3), ("warning", 4), ("error", 5), ("fatal", 6), ("max-severity", 7), ("beta", 8), ("overide", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('mandatory')
if mibBuilder.loadTexts: severity.setDescription('Severity of the logged event.')
message = MibScalar((1, 3, 6, 1, 4, 1, 3405, 10, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: message.setStatus('mandatory')
if mibBuilder.loadTexts: message.setDescription('Content of the logged event.')
mibBuilder.exportSymbols("EXPAND-MANAGEMENT-MIB", log=log, message=message, severity=severity, events=events, general=general)

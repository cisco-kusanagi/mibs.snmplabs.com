#
# PySNMP MIB module ITOUCH-BOOT-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-BOOT-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Bits, iso, TimeTicks, ModuleIdentity, NotificationType, Gauge32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Bits", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xBootClient = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 12))
bootClientStatus = MibScalar((1, 3, 6, 1, 4, 1, 33, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootClientStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bootClientStatus.setDescription('The overall status of the bootstrapping operation, including, for example, what is presently happening and error information.')
mibBuilder.exportSymbols("ITOUCH-BOOT-CLIENT-MIB", bootClientStatus=bootClientStatus, xBootClient=xBootClient)

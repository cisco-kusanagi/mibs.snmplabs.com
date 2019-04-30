#
# PySNMP MIB module ITOUCH-BOOT-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-BOOT-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Unsigned32, TimeTicks, Integer32, Bits, MibIdentifier, Counter32, iso, ObjectIdentity, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "Bits", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xBootClient = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 12))
bootClientStatus = MibScalar((1, 3, 6, 1, 4, 1, 33, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootClientStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ITOUCH-BOOT-CLIENT-MIB", bootClientStatus=bootClientStatus, xBootClient=xBootClient)

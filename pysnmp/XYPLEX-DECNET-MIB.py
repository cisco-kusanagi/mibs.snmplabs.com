#
# PySNMP MIB module XYPLEX-DECNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-DECNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:39:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212-CONCISE-MIB", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, MibIdentifier, enterprises, Bits, ObjectIdentity, TimeTicks, iso, NotificationType, IpAddress, Counter64, Unsigned32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "MibIdentifier", "enterprises", "Bits", "ObjectIdentity", "TimeTicks", "iso", "NotificationType", "IpAddress", "Counter64", "Unsigned32", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
decnet = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 14))
rcp = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 14, 1))
rcpRemoteAddress = MibScalar((1, 3, 6, 1, 4, 1, 33, 14, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcpRemoteAddress.setStatus('mandatory')
mibBuilder.exportSymbols("XYPLEX-DECNET-MIB", xyplex=xyplex, rcpRemoteAddress=rcpRemoteAddress, decnet=decnet, rcp=rcp)

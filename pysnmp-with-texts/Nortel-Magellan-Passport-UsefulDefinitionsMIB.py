#
# PySNMP MIB module Nortel-Magellan-Passport-UsefulDefinitionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-UsefulDefinitionsMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:26:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Unsigned32, IpAddress, enterprises, Counter32, Bits, iso, ModuleIdentity, Gauge32, ObjectIdentity, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Unsigned32", "IpAddress", "enterprises", "Counter32", "Bits", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortel = MibIdentifier((1, 3, 6, 1, 4, 1, 562))
magellan = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1))
passport = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4))
passport50 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1, 1))
passport160 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1, 2))
meridianPassport = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1, 8))
passport30 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1, 11))
passportVirtualRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 1, 12))
components = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1))
passportMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2))
usefulDefinitionsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1))
passportTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3))
usefulDefinitionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1))
usefulDefinitionsGroupBC = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3))
usefulDefinitionsGroupBC03 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3, 3))
usefulDefinitionsGroupBC03A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3, 3, 2))
usefulDefinitionsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3))
usefulDefinitionsCapabilitiesBC = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3))
usefulDefinitionsCapabilitiesBC03 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3, 3))
usefulDefinitionsCapabilitiesBC03A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3, 3, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", passportMIBs=passportMIBs, passportTraps=passportTraps, meridianPassport=meridianPassport, components=components, passportVirtualRouter=passportVirtualRouter, usefulDefinitionsGroupBC03A=usefulDefinitionsGroupBC03A, passport30=passport30, usefulDefinitionsGroupBC=usefulDefinitionsGroupBC, usefulDefinitionsCapabilitiesBC=usefulDefinitionsCapabilitiesBC, usefulDefinitionsCapabilities=usefulDefinitionsCapabilities, usefulDefinitionsGroupBC03=usefulDefinitionsGroupBC03, products=products, passport160=passport160, usefulDefinitionsGroup=usefulDefinitionsGroup, nortel=nortel, magellan=magellan, usefulDefinitionsCapabilitiesBC03A=usefulDefinitionsCapabilitiesBC03A, passport50=passport50, usefulDefinitionsCapabilitiesBC03=usefulDefinitionsCapabilitiesBC03, passport=passport, usefulDefinitionsMIB=usefulDefinitionsMIB)

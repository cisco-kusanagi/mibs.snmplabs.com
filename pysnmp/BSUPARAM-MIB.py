#
# PySNMP MIB module BSUPARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUPARAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, IpAddress, NotificationType, ObjectIdentity, Integer32, Unsigned32, iso, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuParam = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 8))
if mibBuilder.loadTexts: aniBsuParam.setLastUpdated('0111121130Z')
if mibBuilder.loadTexts: aniBsuParam.setOrganization('Aperto Networks')
aniBsuDhcpParamSource = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("server", 2))).clone('server')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuDhcpParamSource.setStatus('current')
mibBuilder.exportSymbols("BSUPARAM-MIB", aniBsuDhcpParamSource=aniBsuDhcpParamSource, aniBsuParam=aniBsuParam, PYSNMP_MODULE_ID=aniBsuParam)

#
# PySNMP MIB module CODAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CODAN-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, enterprises, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Counter64, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "enterprises", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codanGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 23304))
codanGroup.setRevisions(('2009-02-11 00:00',))
if mibBuilder.loadTexts: codanGroup.setLastUpdated('200902110000Z')
if mibBuilder.loadTexts: codanGroup.setOrganization('Codan Limited.')
codanMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 1))
satcomMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 23304, 2))
mibBuilder.exportSymbols("CODAN-SMI", satcomMibs=satcomMibs, codanMibs=codanMibs, codanGroup=codanGroup, PYSNMP_MODULE_ID=codanGroup)

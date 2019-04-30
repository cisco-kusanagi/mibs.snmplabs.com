#
# PySNMP MIB module APTIS-EXPERIMENTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APTIS-EXPERIMENTAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Boolean, aptis_exp = mibBuilder.importSymbols("APTIS-MIB", "Boolean", "aptis-exp")
aptis_modules, = mibBuilder.importSymbols("APTIS-REG-MIB", "aptis-modules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, MibIdentifier, IpAddress, Bits, iso, TimeTicks, NotificationType, ObjectIdentity, Gauge32, Unsigned32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "Bits", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
aptisExpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2637, 1, 1, 6))
if mibBuilder.loadTexts: aptisExpModule.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: aptisExpModule.setOrganization('Aptis Communications, Inc.')
mibBuilder.exportSymbols("APTIS-EXPERIMENTAL-MIB", PYSNMP_MODULE_ID=aptisExpModule, aptisExpModule=aptisExpModule)

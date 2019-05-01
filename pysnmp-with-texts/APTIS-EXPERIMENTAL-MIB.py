#
# PySNMP MIB module APTIS-EXPERIMENTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APTIS-EXPERIMENTAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Boolean, aptis_exp = mibBuilder.importSymbols("APTIS-MIB", "Boolean", "aptis-exp")
aptis_modules, = mibBuilder.importSymbols("APTIS-REG-MIB", "aptis-modules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Bits, TimeTicks, Integer32, Unsigned32, iso, Counter32, MibIdentifier, IpAddress, Gauge32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "Unsigned32", "iso", "Counter32", "MibIdentifier", "IpAddress", "Gauge32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
aptisExpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2637, 1, 1, 6))
if mibBuilder.loadTexts: aptisExpModule.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: aptisExpModule.setOrganization('Aptis Communications, Inc.')
if mibBuilder.loadTexts: aptisExpModule.setContactInfo(' Customer Service Department Aptis Communications, Inc. Email: support@aptis.com')
if mibBuilder.loadTexts: aptisExpModule.setDescription('The following variables describe the administrative actions that may be invoked through SNMP.')
mibBuilder.exportSymbols("APTIS-EXPERIMENTAL-MIB", PYSNMP_MODULE_ID=aptisExpModule, aptisExpModule=aptisExpModule)

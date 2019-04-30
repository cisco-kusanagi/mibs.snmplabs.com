#
# PySNMP MIB module SHASTA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHASTA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Counter64, IpAddress, ModuleIdentity, enterprises, ObjectName, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter32, Bits, Gauge32, Unsigned32, snmpModules, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "IpAddress", "ModuleIdentity", "enterprises", "ObjectName", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter32", "Bits", "Gauge32", "Unsigned32", "snmpModules", "ObjectIdentity", "MibIdentifier")
TimeStamp, TextualConvention, TruthValue, DisplayString, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TruthValue", "DisplayString", "TestAndIncr")
shasta = ModuleIdentity((1, 3, 6, 1, 4, 1, 3199))
shasta.setRevisions(('1999-01-10 00:00',))
if mibBuilder.loadTexts: shasta.setLastUpdated('9907140000Z')
if mibBuilder.loadTexts: shasta.setOrganization('Nortel Networks Shasta IP Services Business Unit')
shastaMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3199, 1))
if mibBuilder.loadTexts: shastaMgmt.setStatus('current')
shastaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 3199, 10))
if mibBuilder.loadTexts: shastaExperiment.setStatus('current')
mibBuilder.exportSymbols("SHASTA-MIB", shasta=shasta, PYSNMP_MODULE_ID=shasta, shastaExperiment=shastaExperiment, shastaMgmt=shastaMgmt)

#
# PySNMP MIB module SHASTA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHASTA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Bits, enterprises, ObjectIdentity, Unsigned32, Counter32, ModuleIdentity, ObjectName, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, Gauge32, snmpModules, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "enterprises", "ObjectIdentity", "Unsigned32", "Counter32", "ModuleIdentity", "ObjectName", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "Gauge32", "snmpModules", "NotificationType")
TextualConvention, TruthValue, DisplayString, TestAndIncr, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TestAndIncr", "TimeStamp")
shasta = ModuleIdentity((1, 3, 6, 1, 4, 1, 3199))
shasta.setRevisions(('1999-01-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: shasta.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: shasta.setLastUpdated('9907140000Z')
if mibBuilder.loadTexts: shasta.setOrganization('Nortel Networks Shasta IP Services Business Unit')
if mibBuilder.loadTexts: shasta.setContactInfo(' Nortel Networks Shasta IP Services Business Unit Customer Service Postal: 2305 Mission College Boulevard Mailstop SC9-C1200 Santa Clara, CA 94054 USA Tel: +1 408 855-3800 E-mail: support@shastanets.com')
if mibBuilder.loadTexts: shasta.setDescription('The Structure of Management Information for the Shasta Networks enterprise.')
shastaMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3199, 1))
if mibBuilder.loadTexts: shastaMgmt.setStatus('current')
if mibBuilder.loadTexts: shastaMgmt.setDescription('shastaMgmt is the main subtree for new mib development.')
shastaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 3199, 10))
if mibBuilder.loadTexts: shastaExperiment.setStatus('current')
if mibBuilder.loadTexts: shastaExperiment.setDescription('shastaExperiment provides a root object identifier from which experimental MIBs may be temporarily based. MIBs are typicially based here if they fall in one of two categories 1) are IETF work-in-process MIBs which have not been assigned a permanent object identifier by the IANA. 2) are shasta work-in-process which has not been assigned a permanent object identifier by the shasat assigned number authority, typicially because the mib is not ready for deployment. NOTE WELL: support for MIBs in the shastaExperiment subtree will be deleted when a permanent object identifier assignment is made.')
mibBuilder.exportSymbols("SHASTA-MIB", shastaExperiment=shastaExperiment, PYSNMP_MODULE_ID=shasta, shasta=shasta, shastaMgmt=shastaMgmt)

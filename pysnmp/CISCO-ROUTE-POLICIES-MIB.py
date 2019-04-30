#
# PySNMP MIB module CISCO-ROUTE-POLICIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ROUTE-POLICIES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Integer32, Unsigned32, Counter64, ObjectIdentity, NotificationType, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Integer32", "Unsigned32", "Counter64", "ObjectIdentity", "NotificationType", "iso", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRoutePoliciesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578))
ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setLastUpdated('200608180000Z')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setOrganization('Cisco Systems, Inc. ')
ciscoRoutePoliciesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 0))
ciscoRoutePoliciesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 1))
ciscoRoutePoliciesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 2))
crpPolicies = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1))
if mibBuilder.loadTexts: crpPolicies.setStatus('current')
crpPolicyIfIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1))
if mibBuilder.loadTexts: crpPolicyIfIndex.setStatus('current')
mibBuilder.exportSymbols("CISCO-ROUTE-POLICIES-MIB", ciscoRoutePoliciesMIB=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIBObjects=ciscoRoutePoliciesMIBObjects, PYSNMP_MODULE_ID=ciscoRoutePoliciesMIB, crpPolicyIfIndex=crpPolicyIfIndex, ciscoRoutePoliciesMIBConform=ciscoRoutePoliciesMIBConform, crpPolicies=crpPolicies, ciscoRoutePoliciesMIBNotifs=ciscoRoutePoliciesMIBNotifs)

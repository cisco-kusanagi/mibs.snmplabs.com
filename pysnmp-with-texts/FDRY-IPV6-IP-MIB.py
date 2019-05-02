#
# PySNMP MIB module FDRY-IPV6-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-IPV6-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
RtrStatus, = mibBuilder.importSymbols("FOUNDRY-SN-IP-MIB", "RtrStatus")
fdryIpv6, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryIpv6")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, ModuleIdentity, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, MibIdentifier, Bits, Integer32, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "MibIdentifier", "Bits", "Integer32", "iso", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fdryIpv6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1))
fdryIpv6MIB.setRevisions(('2010-07-26 00:00', '2010-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryIpv6MIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', '',))
if mibBuilder.loadTexts: fdryIpv6MIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryIpv6MIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryIpv6MIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryIpv6MIB.setDescription("The Brocade proprietary MIB module for IPv6. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
fdryIpv6GlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1))
fdryIpv6LoadShare = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 1), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShare.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6LoadShare.setDescription('If more than one ipv6 route available, use them to share load.')
fdryIpv6LoadShareNumOfPaths = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShareNumOfPaths.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6LoadShareNumOfPaths.setDescription('Number of ipv6 routes are used to share load.')
mibBuilder.exportSymbols("FDRY-IPV6-IP-MIB", fdryIpv6LoadShareNumOfPaths=fdryIpv6LoadShareNumOfPaths, fdryIpv6MIB=fdryIpv6MIB, fdryIpv6LoadShare=fdryIpv6LoadShare, fdryIpv6GlobalObjects=fdryIpv6GlobalObjects, PYSNMP_MODULE_ID=fdryIpv6MIB)

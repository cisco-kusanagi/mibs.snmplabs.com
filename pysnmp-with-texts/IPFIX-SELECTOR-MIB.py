#
# PySNMP MIB module IPFIX-SELECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFIX-SELECTOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:55:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Bits, Integer32, Gauge32, Unsigned32, IpAddress, MibIdentifier, TimeTicks, mib_2, NotificationType, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "mib-2", "NotificationType", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ipfixSelectorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 194))
ipfixSelectorMIB.setRevisions(('2012-06-11 00:00', '2010-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipfixSelectorMIB.setRevisionsDescriptions(('Update to MIB description to reflect updated registration of new Sampling and Filtering functions. Published as RFC 6615.', 'Initial version, published as RFC 5815.',))
if mibBuilder.loadTexts: ipfixSelectorMIB.setLastUpdated('201206110000Z')
if mibBuilder.loadTexts: ipfixSelectorMIB.setOrganization('IETF IPFIX Working Group')
if mibBuilder.loadTexts: ipfixSelectorMIB.setContactInfo('WG charter: http://www.ietf.org/html.charters/ipfix-charter.html Mailing Lists: General Discussion: ipfix@ietf.org To Subscribe: http://www1.ietf.org/mailman/listinfo/ipfix Archive: http://www1.ietf.org/mail-archive/web/ipfix/current/index.html Editor: Thomas Dietz NEC Europe Ltd. NEC Laboratories Europe Network Research Division Kurfuersten-Anlage 36 Heidelberg 69115 Germany Phone: +49 6221 4342-128 Email: Thomas.Dietz@neclab.eu Atsushi Kobayashi NTT Information Sharing Platform Laboratories 3-9-11 Midori-cho Musashino-shi, Tokyo 180-8585 Japan Phone: +81-422-59-3978 Email: akoba@nttv6.net Benoit Claise Cisco Systems, Inc. De Kleetlaan 6a b1 Diegem 1831 Belgium Phone: +32 2 704 5622 Email: bclaise@cisco.com Gerhard Muenz Technische Universitaet Muenchen Department of Informatics Chair for Network Architectures and Services (I8) Boltzmannstr. 3 Garching 85748 Germany Email: muenz@net.in.tum.de')
if mibBuilder.loadTexts: ipfixSelectorMIB.setDescription("The IPFIX SELECTOR MIB module defined in this section provides the standard Filtering and Sampling functions that can be referenced in the ipfixSelectionProcessTable. All standard Filtering and Sampling functions MUST be registered in the subtree under object ipfixSelectorFunctions (1.3.6.1.2.1.194.1.1). The top-level OIDs in the subtree under object ipfixSelectorFunctions MUST be registered in a sub-registry maintained by IANA at <http://www.iana.org/assignments/smi-numbers/>. New Selector Functions MUST be registered at IANA and are subject to Expert Review [RFC5226], i.e., review by one of a group of experts designated by an IETF Area Director. The group of experts MUST check the requested MIB objects for completeness and accuracy of the description. Requests for MIB objects that duplicate the functionality of existing objects SHOULD be declined. The smallest available OID SHOULD be assigned to new MIB objects. The specification of new MIB objects SHOULD follow the structure specified in [RFC6615] and MUST be published using a well- established and persistent publication medium. The experts will initially be drawn from the Working Group Chairs and document editors of the IPFIX and PSAMP Working Groups. Copyright (c) 2012 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
ipfixSelectorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1))
ipfixSelectorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2))
ipfixSelectorFunctions = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1))
ipfixFuncSelectAll = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 1))
ipfixFuncSelectAllAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixFuncSelectAllAvail.setStatus('current')
if mibBuilder.loadTexts: ipfixFuncSelectAllAvail.setDescription('This object indicates the availability of the trivial function of selecting all packets. This function is always available.')
ipfixSelectorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 1))
ipfixSelectorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 2))
ipfixSelectorBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 194, 2, 1, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixSelectorBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicCompliance = ipfixSelectorBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: ipfixSelectorBasicCompliance.setDescription('An implementation that builds an IPFIX Exporter that complies with this module MUST implement the objects defined in the mandatory group ipfixBasicGroup. The implementation of all other objects depends on the implementation of the corresponding functionality in the equipment.')
ipfixSelectorBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 194, 2, 2, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixFuncSelectAllAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicGroup = ipfixSelectorBasicGroup.setStatus('current')
if mibBuilder.loadTexts: ipfixSelectorBasicGroup.setDescription('The main IPFIX objects.')
mibBuilder.exportSymbols("IPFIX-SELECTOR-MIB", ipfixSelectorGroups=ipfixSelectorGroups, ipfixFuncSelectAll=ipfixFuncSelectAll, ipfixSelectorCompliances=ipfixSelectorCompliances, ipfixSelectorBasicCompliance=ipfixSelectorBasicCompliance, ipfixSelectorConformance=ipfixSelectorConformance, ipfixSelectorObjects=ipfixSelectorObjects, PYSNMP_MODULE_ID=ipfixSelectorMIB, ipfixFuncSelectAllAvail=ipfixFuncSelectAllAvail, ipfixSelectorBasicGroup=ipfixSelectorBasicGroup, ipfixSelectorMIB=ipfixSelectorMIB, ipfixSelectorFunctions=ipfixSelectorFunctions)

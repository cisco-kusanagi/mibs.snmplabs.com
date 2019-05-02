#
# PySNMP MIB module TPT-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Counter64, NotificationType, Gauge32, Integer32, Bits, IpAddress, iso, MibIdentifier, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "Integer32", "Bits", "IpAddress", "iso", "MibIdentifier", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_sflow_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18)).setLabel("tpt-sflow-objs")
tpt_sflow_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_sflow_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_sflow_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_sflow_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_sflow_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_sflow_objs.setDescription("Global sFlow status and collector address/udp port on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class SflowStatus(TextualConvention, Integer32):
    description = 'An indication of sFlow enable/disable/applicable status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

sFlowCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1), )
if mibBuilder.loadTexts: sFlowCollectorTable.setStatus('current')
if mibBuilder.loadTexts: sFlowCollectorTable.setDescription('Table of sFlow collectors. It supports up to 2 collectors.')
sFlowCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1), ).setIndexNames((0, "TPT-SFLOW-MIB", "collectorIndex"))
if mibBuilder.loadTexts: sFlowCollectorEntry.setStatus('current')
if mibBuilder.loadTexts: sFlowCollectorEntry.setDescription('A collector address and port in the sFlowCollectorTable. Rows cannot be created or deleted. ')
collectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: collectorIndex.setStatus('current')
if mibBuilder.loadTexts: collectorIndex.setDescription('Index into the sFlow collector table, starting with 1.')
collectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddr.setStatus('current')
if mibBuilder.loadTexts: collectorAddr.setDescription('The IPv4 address of the collector. If the address is not set, the value will be an empty string. It is not applicable on platforms (10/110/330). For those platforms, the value will be set to an empty string. ')
udpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpPort.setStatus('current')
if mibBuilder.loadTexts: udpPort.setDescription('The udp port of the collector. It is not applicable on Lowball platforms (10/110/330). For those platforms, the value will be set to 0. ')
collectorAddrV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddrV6.setStatus('current')
if mibBuilder.loadTexts: collectorAddrV6.setDescription('The IPv6 address of the collector. If the address is not set, the value will be an empty string. It is not applicable on Lowball platforms (10/110/330). For those platforms, the value will be set to an empty string ')
sFlowStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 2), SflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowStatus.setStatus('current')
if mibBuilder.loadTexts: sFlowStatus.setDescription('A Device-wide sFlow status.')
mibBuilder.exportSymbols("TPT-SFLOW-MIB", PYSNMP_MODULE_ID=tpt_sflow_objs, collectorAddr=collectorAddr, SflowStatus=SflowStatus, sFlowCollectorEntry=sFlowCollectorEntry, sFlowCollectorTable=sFlowCollectorTable, udpPort=udpPort, tpt_sflow_objs=tpt_sflow_objs, sFlowStatus=sFlowStatus, collectorIndex=collectorIndex, collectorAddrV6=collectorAddrV6)

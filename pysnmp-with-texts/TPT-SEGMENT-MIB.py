#
# PySNMP MIB module TPT-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SEGMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, iso, Counter32, TimeTicks, Bits, Integer32, ObjectIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "iso", "Counter32", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_segment_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19)).setLabel("tpt-segment-objs")
tpt_segment_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_segment_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_segment_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_segment_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_segment_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_segment_objs.setDescription("Details of segments on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class SegmentSflowStatus(TextualConvention, Integer32):
    description = 'An indication of sFlow enable/disable/applicable status for a segment'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

segmentTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1), )
if mibBuilder.loadTexts: segmentTable.setStatus('current')
if mibBuilder.loadTexts: segmentTable.setDescription('Table of segment-related information.')
segmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1), ).setIndexNames((0, "TPT-SEGMENT-MIB", "slotIndex"), (0, "TPT-SEGMENT-MIB", "segmentIndex"))
if mibBuilder.loadTexts: segmentEntry.setStatus('current')
if mibBuilder.loadTexts: segmentEntry.setDescription('An entry in the segment table. Rows cannot be created or deleted. ')
slotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIndex.setStatus('current')
if mibBuilder.loadTexts: slotIndex.setDescription('The slot index, starting with 1. For older platforms like N-platforms and Lowball, all the segments are assumed to be on slot 1. ')
segmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentIndex.setStatus('current')
if mibBuilder.loadTexts: segmentIndex.setDescription('The segment index, starting with 1.')
segmentSflowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 3), SegmentSflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentSflowStatus.setStatus('current')
if mibBuilder.loadTexts: segmentSflowStatus.setDescription('sFlow status of the segment. Not applicable on Lowball platforms (10/110/330). For those platforms, the value will be set to not-applicable. ')
sFlowDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowDivisor.setStatus('current')
if mibBuilder.loadTexts: sFlowDivisor.setDescription('The sFlow divisor value of the segment. Not applicable on the Lowball platforms (10/110/330). For those platforms, the value will be set to 0. ')
mibBuilder.exportSymbols("TPT-SEGMENT-MIB", sFlowDivisor=sFlowDivisor, SegmentSflowStatus=SegmentSflowStatus, slotIndex=slotIndex, segmentIndex=segmentIndex, segmentSflowStatus=segmentSflowStatus, PYSNMP_MODULE_ID=tpt_segment_objs, tpt_segment_objs=tpt_segment_objs, segmentEntry=segmentEntry, segmentTable=segmentTable)
